from retriever import retrieve_context

query = "What is SQL Injection?"

context = retrieve_context(query)

print("\nRESULT:\n")
print(context)