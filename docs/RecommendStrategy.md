# RecommendStrategy

How to use positive and negative examples to find the results, default is `average_vector`:  * `average_vector` - Average positive and negative vectors and create a single query with the formula `query = avg_pos + avg_pos - avg_neg`. Then performs normal search.  * `best_score` - Uses custom search objective. Each candidate is compared against all examples, its score is then chosen from the `max(max_pos_score, max_neg_score)`. If the `max_neg_score` is chosen then it is squared and negated, otherwise it is just the `max_pos_score`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


