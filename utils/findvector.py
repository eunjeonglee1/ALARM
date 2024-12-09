def find(retriever,user_food):
    context = retriever.get_relevant_documents(query=user_food)
    return context