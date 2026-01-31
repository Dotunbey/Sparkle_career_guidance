"""
Sparkle Backend Application - Data Models.

This module defines the core data structures using Pydantic and Dataclasses.
It covers Users, IT Domains, Assessments, and Recommendations.
"""

from typing import List, Dict
from uuid import UUID, uuid4
from enum import Enum
from dataclasses import dataclass, field
from pydantic import BaseModel, EmailStr, Field, validator


class EmotionalStage(str, Enum):
    """Enum representing the stages in the Emotional Cycle of Change."""
    UNINFORMED_OPTIMISM = "Uninformed Optimism"
    INFORMED_PESSIMISM = "Informed Pessimism"
    VALLEY_OF_DESPAIR = "Valley of Despair"
    INFORMED_OPTIMISM = "Informed Optimism"
    SUCCESS = "Success"


class IkigaiQuadrant(str, Enum):
    """Enum representing the four circles of Ikigai."""
    PASSION = "Passion (Love + Good At)"
    MISSION = "Mission (Love + Needs)"
    VOCATION = "Vocation (Needs + Paid)"
    PROFESSION = "Profession (Good At + Paid)"


class ITSubDomain(BaseModel):
    """
    Represents a specific role or specialization within an IT Domain.
    
    Attributes:
        id: Unique identifier.
        name: Name of the subdomain (e.g., 'Frontend Development').
        description: Brief description.
        required_skills: List of key skills.
    """
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    required_skills: List[str]


class ITDomain(BaseModel):
    """
    Represents a broad area within Information Technology.
    
    Attributes:
        id: Unique identifier.
        name: Name of the domain (e.g., 'Software Development', 'Data Science').
        description: Overview of the domain as a problem-solving tool.
        subdomains: List of associated subdomains.
    """
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    subdomains: List[ITSubDomain] = []

    @property
    def total_subdomains(self) -> int:
        """Returns the count of subdomains."""
        return len(self.subdomains)


class UserProfile(BaseModel):
    """
    Represents a user of the Sparkle platform.
    
    Attributes:
        id: Unique user ID.
        username: Display name.
        email: Contact email.
        current_emotional_stage: Derived from assessment.
        ikigai_inputs: A dictionary representing scores in the 4 Ikigai areas.
    """
    id: UUID = Field(default_factory=uuid4)
    username: str
    email: EmailStr
    current_emotional_stage: EmotionalStage = EmotionalStage.UNINFORMED_OPTIMISM
    # Score 0-10 for: love, good_at, world_needs, paid_for
    ikigai_inputs: Dict[str, int] = Field(default_factory=lambda: {
        "love": 0, "good_at": 0, "world_needs": 0, "paid_for": 0
    })

    @validator('ikigai_inputs')
    def validate_scores(cls, v):
        """Validates that all ikigai input scores are within 0-10 range."""
        for key, value in v.items():
            if not (0 <= value <= 10):
                raise ValueError(f"Score for {key} must be between 0 and 10")
        return v


@dataclass
class CareerRecommendation:
    """
    Data Transfer Object for returning AI recommendations.
    """
    user_id: UUID
    recommended_domains: List[str]
    confidence_score: float
    reasoning: str
    next_steps: List[str] = field(default_factory=list)
