
from enum import Enum
from typing import Dict, List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr, Field, field_validator

# --- Enums ---
class EmotionalStage(str, Enum):
    UNINFORMED_OPTIMISM = "Uninformed Optimism"
    INFORMED_PESSIMISM = "Informed Pessimism"
    VALLEY_OF_DESPAIR = "Valley of Despair"
    INFORMED_OPTIMISM = "Informed Optimism"
    SUCCESS = "Success"

class IkigaiQuadrant(str, Enum):
    PASSION = "Passion"
    MISSION = "Mission"
    VOCATION = "Vocation"
    PROFESSION = "Profession"

class CoursePlatform(str, Enum):
    COURSERA = "Coursera"
    UDEMY = "Udemy"
    YOUTUBE = "YouTube"

# --- Core Domain Models ---
class ITSubDomain(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    required_skills: List[str]

class ITDomain(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    subdomains: List[ITSubDomain] = Field(default_factory=list)

class UserProfile(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: EmailStr
    ikigai_inputs: Dict[str, int] = Field(
        default_factory=lambda: {"love": 0, "good_at": 0, "world_needs": 0, "paid_for": 0}
    )

    # UPDATED FOR PYDANTIC V2
    @field_validator("ikigai_inputs")
    @classmethod
    def validate_scores(cls, v: Dict[str, int]) -> Dict[str, int]:
        for k, score in v.items():
            if not (0 <= score <= 10):
                raise ValueError(f"Score for {k} must be between 0 and 10")
        return v

class Course(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    platform: CoursePlatform
    url: str
    level: str
    duration_hours: float
    subdomain: str

class CourseProgress(BaseModel):
    user_id: UUID
    course_id: UUID
    progress_percent: int = 0

# --- API Response Models ---
class CourseResponse(BaseModel):
    id: UUID
    title: str
    platform: CoursePlatform
    url: str
    level: str
    duration_hours: float
    emotional_stage: EmotionalStage
    progress: int

class RecommendationResponse(BaseModel):
    user_id: UUID
    domains: List[str]
    reasoning: str
    confidence_score: float
    courses: List[CourseResponse]

class ProgressUpdateRequest(BaseModel):
    user_id: UUID
    course_id: UUID
    progress: int
