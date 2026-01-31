"""
Sparkle Backend Application - Business Logic Services.

This module implements the core logic for Assessments, Domain Management,
and Recommendation generation.
"""

import logging
from typing import List, Optional
from .models import (
    UserProfile, ITDomain, ITSubDomain, 
    EmotionalStage, CareerRecommendation, IkigaiQuadrant
)

logger = logging.getLogger(__name__)


class ITDomainService:
    """
    Manages IT Domains and Subdomains data.
    Acts as a repository wrapper (in-memory for this example).
    """

    def __init__(self):
        self._domains: List[ITDomain] = self._seed_data()

    def _seed_data(self) -> List[ITDomain]:
        """Seeds initial data for the application."""
        return [
            ITDomain(
                name="Software Development",
                description="Building digital tools to solve human problems.",
                subdomains=[
                    ITSubDomain(name="Frontend", description="Visual interface", required_skills=["React", "CSS"]),
                    ITSubDomain(name="Backend", description="Server logic", required_skills=["Python", "SQL"])
                ]
            ),
            ITDomain(
                name="Data Science",
                description="Extracting insights from chaos to drive decisions.",
                subdomains=[
                    ITSubDomain(name="Machine Learning", description="Predictive models", required_skills=["Stats", "Python"]),
                    ITSubDomain(name="Data Analysis", description="Business insights", required_skills=["Excel", "SQL"])
                ]
            ),
            ITDomain(
                name="Cybersecurity",
                description="Protecting digital assets and privacy.",
                subdomains=[
                    ITSubDomain(name="Penetration Testing", description="Ethical hacking", required_skills=["Networking", "Linux"])
                ]
            )
        ]

    def get_all_domains(self) -> List[ITDomain]:
        """Retrieves all available IT domains."""
        return self._domains

    def get_domain_by_name(self, name: str) -> Optional[ITDomain]:
        """
        Finds a domain by name (case-insensitive).
        
        Args:
            name: The name of the domain to search for.
            
        Returns:
            ITDomain object or None if not found.
        """
        normalized_name = name.lower()
        # Using generator expression for memory efficiency if list was large
        return next(
            (d for d in self._domains if d.name.lower() == normalized_name), 
            None
        )


class AssessmentService:
    """
    Handles psychological framework logic (Ikigai, Emotional Cycle).
    """

    @staticmethod
    def calculate_ikigai_quadrant(user: UserProfile) -> IkigaiQuadrant:
        """
        Determines the user's dominant Ikigai quadrant based on input scores.
        
        Logic:
        - Passion: High Love + High Skill
        - Mission: High Love + High Need
        - Vocation: High Need + High Pay
        - Profession: High Skill + High Pay
        """
        s = user.ikigai_inputs
        
        # Simple heuristic: sum pairs to find dominant quadrant
        scores = {
            IkigaiQuadrant.PASSION: s["love"] + s["good_at"],
            IkigaiQuadrant.MISSION: s["love"] + s["world_needs"],
            IkigaiQuadrant.VOCATION: s["world_needs"] + s["paid_for"],
            IkigaiQuadrant.PROFESSION: s["good_at"] + s["paid_for"],
        }
        
        # Return the key with the max value
        return max(scores, key=scores.get)

    @staticmethod
    def determine_emotional_stage(confidence_level: int, competence_level: int) -> EmotionalStage:
        """
        Maps user confidence/competence to the Emotional Cycle of Change.
        
        Args:
            confidence_level (1-10): User's self-reported confidence.
            competence_level (1-10): User's actual skill/competence.
            
        Returns:
            EmotionalStage enum.
        """
        if confidence_level > 7 and competence_level < 3:
            return EmotionalStage.UNINFORMED_OPTIMISM
        elif confidence_level < 5 and competence_level < 5:
            return EmotionalStage.INFORMED_PESSIMISM
        elif confidence_level < 3 and competence_level > 5:
            return EmotionalStage.VALLEY_OF_DESPAIR
        elif confidence_level > 6 and competence_level > 7:
            return EmotionalStage.SUCCESS
        else:
            return EmotionalStage.INFORMED_OPTIMISM


class AIRecommendationService:
    """
    Mock AI Service to generate career recommendations.
    In production, this would wrap calls to OpenAI/Gemini/Claude.
    """

    def __init__(self, domain_service: ITDomainService):
        self.domain_service = domain_service

    def generate_recommendation(self, user: UserProfile) -> CareerRecommendation:
        """
        Generates a personalized career recommendation based on user profile.
        
        Args:
            user: The user profile containing assessment data.
            
        Returns:
            CareerRecommendation object.
        """
        logger.info(f"Generating AI recommendation for user: {user.username}")
        
        # Simulate AI Logic: Rule-based matching for MVP
        quadrant = AssessmentService.calculate_ikigai_quadrant(user)
        recommended_domains = []
        reasoning = ""

        all_domains = self.domain_service.get_all_domains()

        if quadrant == IkigaiQuadrant.PASSION:
            # Passionate users might enjoy creative building
            recommended_domains = [d.name for d in all_domains if "Software" in d.name]
            reasoning = f"Your profile indicates a strong 'Passion' alignment. {recommended_domains[0]} allows you to build what you love using your skills."
        
        elif quadrant == IkigaiQuadrant.PROFESSION:
            # Profession focused users might like stable, high-skill fields
            recommended_domains = [d.name for d in all_domains if "Data" in d.name or "Security" in d.name]
            reasoning = "You align with 'Profession'. Data & Security offer structured environments to leverage your high competency for reward."
            
        else:
            # Default fallback logic
            recommended_domains = [d.name for d in all_domains]
            reasoning = "Your profile is balanced. We recommend exploring broad problem-solving disciplines."

        return CareerRecommendation(
            user_id=user.id,
            recommended_domains=recommended_domains,
            confidence_score=0.85, # Mock confidence
            reasoning=reasoning,
            next_steps=["Take the 'Intro to IT' module", "Watch day-in-the-life videos"]
        )
