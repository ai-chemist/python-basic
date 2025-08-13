import pytest
from survey import AnonymousSurvey

# 데코레이터 사용 - 픽스쳐(fixture) 테스트 리소스 공유
@pytest.fixture
def name_survey():
    """모든 응답에 사용 가능"""
    question = "What is your name?"
    name_survey = AnonymousSurvey(question)
    return name_survey

def test_store_single_response(name_survey):
    """단일 응답 테스트"""
    # question = "What is your name?"
    # name_survey = AnonymousSurvey(question)
    name_survey.store_response('John')
    assert 'John' in name_survey.response

def test_store_multiple_responses(name_survey):
    """복수 응답 테스트"""
    # question = "What is your name?"
    # name_survey = AnonymousSurvey(question)
    responses = ['Red', 'Green', 'Blue']
    for response in responses:
        name_survey.store_response(response)

    for response in responses:
        assert response in name_survey.response