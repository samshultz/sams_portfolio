import datetime
import pytest
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from core.models import WorkExperience, Skill, TechStack

def test_experience_start_date_with_future_date_returns_error(db):
    today = datetime.date.today()
    start_date = datetime.date(today.year, today.month, today.day+1)

    with pytest.raises(ValidationError):
        experience = WorkExperience.objects.create(
            position="Junior Web Developer",
            company="Credpal",
            start_date=start_date,
            end_date=today,
            description="hello to you",
            currently_working_here=False
        )
   

def test_experience_end_date_cant_be_future_date(db):
    today = datetime.date.today()
    end_date = datetime.date(today.year, today.month, today.day+1)

    with pytest.raises(ValidationError):
        experience = WorkExperience.objects.create(
            position="Junior Web Developer",
            company="Credpal",
            start_date=datetime.date.today(),
            end_date=end_date,
            description="hello to you",
            currently_working_here=False
        )

def test_experience_start_date_cant_be_greater_than_end_date(db):
    today = datetime.date.today()
    start_date = datetime.date(today.year-1, today.month, today.day+1)
    end_date = datetime.date(today.year-2, today.month, today.day)
    
    with pytest.raises(ValidationError):
        experience = WorkExperience.objects.create(
            position="Junior Web Developer",
            company="Credpal",
            start_date=start_date,
            end_date=end_date,
            description="hello to you",
            currently_working_here=False
        )

def test_one_of_both_end_date_or_presently_working_here_set(db):
     with pytest.raises(ValidationError):
        experience = WorkExperience.objects.create(
            position="Junior Web Developer",
            company="Credpal",
            start_date=datetime.date.today(),
            description="hello to you",
            currently_working_here=False
        )


def test_both_end_date_and_presently_working_here_cant_be_set_thesame_time(db):
    today = datetime.date.today()
    start_date = datetime.date(today.year-1, today.month, today.day+1)
    end_date = datetime.date(today.year, today.month, today.day)

    with pytest.raises(ValidationError):
        experience = WorkExperience.objects.create(
            position="Junior Web Developer",
            company="Credpal",
            start_date=start_date,
            end_date=end_date,
            description="hello to you",
            currently_working_here=True
        )

def test_str_representation_of_work_experience(db):
    today = datetime.date.today()
    start_date = datetime.date(today.year-1, today.month, today.day+1)
    end_date = datetime.date(today.year, today.month, today.day)

    experience = WorkExperience.objects.create(
        position="Junior Web Developer",
        company="Credpal",
        start_date=start_date,
        end_date=end_date,
        description="hello to you",
        currently_working_here=False
    )
    assert "Junior Web Developer at Credpal" == str(experience)

def test_str_representation_of_skill(db):
    skill = Skill.objects.create(name="Web development", description="creating stunning platforms")
    assert "Web development" == str(skill)

def test_str_representation_of_tech_stack(db):
    stack = TechStack.objects.create(name="HTML")
    assert "HTML" == str(stack)