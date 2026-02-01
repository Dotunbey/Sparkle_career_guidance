#!filepath services.py
from typing import Dict, List, Optional
from uuid import UUID
from models import (
    Course, CoursePlatform, CourseProgress, EmotionalStage, 
    IkigaiQuadrant, ITDomain, ITSubDomain, UserProfile
)

class DomainRepository:
    def __init__(self) -> None:
        self._domains = [
            ITDomain(name="Software Development", subdomains=[
                ITSubDomain(name="Frontend", required_skills=["React", "CSS"]),
                ITSubDomain(name="Backend", required_skills=["Python", "FastAPI"])
            ]),
            ITDomain(name="Data Science", subdomains=[
                ITSubDomain(name="ML Engineering", required_skills=["PyTorch", "Math"])
            ])
        ]
    
    def all(self) -> List[ITDomain]:
        return self._domains

class CourseRepository:
    def __init__(self) -> None:
        self._courses = [
            Course(title="React Zero to Hero", platform=CoursePlatform.YOUTUBE, url="http://yt.com", level="Beginner", duration_hours=5, subdomain="Frontend"),
            Course(title="FastAPI Web Dev", platform=CoursePlatform.UDEMY, url="http://udemy.com", level="Intermediate", duration_hours=12, subdomain="Backend"),
        ]

    def by_subdomain(self, subdomain: str) -> List[Course]:
        return [c for c in self._courses if c.subdomain == subdomain]

class AssessmentService:
    @staticmethod
    def ikigai_quadrant(user: UserProfile) -> IkigaiQuadrant:
        s = user.ikigai_inputs
        scores = {
            IkigaiQuadrant.PASSION: s["love"] + s["good_at"],
            IkigaiQuadrant.MISSION: s["love"] + s["world_needs"],
            IkigaiQuadrant.VOCATION: s["world_needs"] + s["paid_for"],
            IkigaiQuadrant.PROFESSION: s["good_at"] + s["paid_for"],
        }
        return max(scores, key=scores.get) # type: ignore

    @staticmethod
    def predict_emotional_stage(progress: int) -> EmotionalStage:
        if progress < 20: return EmotionalStage.UNINFORMED_OPTIMISM
        if progress < 40: return EmotionalStage.INFORMED_PESSIMISM
        if progress < 60: return EmotionalStage.VALLEY_OF_DESPAIR
        if progress < 90: return EmotionalStage.INFORMED_OPTIMISM
        return EmotionalStage.SUCCESS

class ProgressService:
    def __init__(self) -> None:
        # In-memory DB for demo: { (user_id, course_id): percent }
        self._store: Dict[str, int] = {}

    def get_progress(self, user_id: UUID, course_id: UUID) -> int:
        key = f"{user_id}:{course_id}"
        return self._store.get(key, 0)

    def update_progress(self, user_id: UUID, course_id: UUID, percent: int) -> EmotionalStage:
        key = f"{user_id}:{course_id}"
        self._store[key] = min(max(percent, 0), 100)
        return AssessmentService.predict_emotional_stage(self._store[key])
