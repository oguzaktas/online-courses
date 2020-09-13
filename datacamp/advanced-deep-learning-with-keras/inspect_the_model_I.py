'''
Instructions
- Print the model's weights.
- Print the column means of the training data (games_tourney_train).
'''

# Print the model's weights
print(model.get_weights())

# Print the column means of the training data
print(games_tourney_train.mean())

'''
Output:
<script.py> output:
    [array([[ 0.13067713, -0.10371894],
           [ 0.38644195, -0.35632333]], dtype=float32), array([72.38115, 72.38473], dtype=float32)]
    season        1.998074e+03
    team_1        5.556771e+03
    team_2        5.556771e+03
    home          0.000000e+00
    seed_diff     0.000000e+00
    score_diff    0.000000e+00
    score_1       7.162128e+01
    score_2       7.162128e+01
    won           5.000000e-01
    pred         -1.625470e-14
    dtype: float64
'''    