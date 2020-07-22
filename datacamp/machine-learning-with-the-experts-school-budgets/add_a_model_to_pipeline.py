'''
Instructions
- Complete the 'numeric_features' transform with the following steps:
    - get_numeric_data, with the name 'selector'.
    - Imputer(), with the name 'imputer'.
- Complete the 'text_features' transform with the following steps:
    - get_text_data, with the name 'selector'.
    - CountVectorizer(), with the name 'vectorizer'.
- Fit the pipeline to the training data.
- Hit 'Submit Answer' to compute the accuracy!
'''

# Complete the pipeline: pl
pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list = [
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', Imputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer())
                ]))
             ]
        )),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

# Fit to the training data
pl.fit(X_train, y_train)

# Compute and print accuracy
accuracy = pl.score(X_test, y_test)
print("\nAccuracy on budget dataset: ", accuracy)
