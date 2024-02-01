from image_generator.models import ImageGeneration
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def enrich_document(image_gen):
    # Start with the headline and repeat it to give it more weight
    document = [image_gen.news_context.headline] * 3  # Weighting headline more
    
    # Add keywords, subcategory, category, emotion tone, and other fields
    document += [kw.word for kw in image_gen.news_context.keywords.all()] * 2  # Double weight for keywords
    document += [sub.name for sub in image_gen.news_context.subcategories.all()]
    document += [image_gen.news_context.category, image_gen.news_context.emotionTone]
    document += [image_gen.news_context.geographicalContext]
    document += [char.type + ' ' + char.action for char in image_gen.visual_elements.characters.all()]
    
    # Add object details
    document += [od.description for od in image_gen.visual_elements.object_details.all()]
    
    # Join all parts into a single string
    return ' '.join(document)

def find_similar_image_generations(selected_image_generation_id):
    target_image_generation = ImageGeneration.objects.get(id=selected_image_generation_id)
    all_image_generations = ImageGeneration.objects.exclude(id=selected_image_generation_id)
    
    # Create enriched documents
    documents = [enrich_document(target_image_generation)]
    documents_ids = [selected_image_generation_id]
    
    for gen in all_image_generations:
        documents.append(enrich_document(gen))
        documents_ids.append(gen.id)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    target_vector = tfidf_matrix[0]
    comparison_vectors = tfidf_matrix[1:]

    similarities = cosine_similarity(target_vector, comparison_vectors)[0]

    # Collect and sort by similarity score
    similar_objects_with_scores = [(gen.id, score) for gen, score in zip(all_image_generations, similarities)]
    similar_objects_with_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Fetch and pair with scores
    results = []
    for obj_id, score in similar_objects_with_scores:
        if score > 0.15:
          obj = ImageGeneration.objects.get(id=obj_id)
          results.append((obj, score*100))

    return results