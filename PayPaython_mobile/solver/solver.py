def mp_verify(challenge_type, response):
    """Verifies the response for a given challenge type."""
    if challenge_type in CHALLENGE_TYPES:
        expected_response = CHALLENGE_TYPES[challenge_type]
        return response == expected_response
    return False

CHALLENGE_TYPES = {
    'challenge_1': 'expected_response_1',
    'challenge_2': 'expected_response_2',
    # Add more challenges as needed
}