"""
Sparkle Backend Application - Entry Point.

This script demonstrates the usage of the Sparkle modules to create a user,
assess their profile, and generate a career recommendation.
"""

import logging
from .models import UserProfile
from .services import ITDomainService, AIRecommendationService, AssessmentService

# Configure logger for main execution
logger = logging.getLogger("SparkleApp")
logging.basicConfig(level=logging.INFO)

def main():
    """
    Main execution flow simulating a user journey on Sparkle.
    """
    logger.info("Starting Sparkle Career Guidance System...")

    # 1. Initialize Services
    domain_service = ITDomainService()
    ai_service = AIRecommendationService(domain_service)

    # 2. Simulate User Creation (Student entering IT)
    try:
        user = UserProfile(
            username="Alex_Student",
            email="alex@university.edu",
            ikigai_inputs={
                "love": 9,        # Loves tech
                "good_at": 7,     # Decent coding skills
                "world_needs": 5, # Unsure of market need
                "paid_for": 8     # Knows it pays well
            }
        )
        logger.info(f"User created: {user.username} | Email: {user.email}")
    except ValueError as e:
        logger.error(f"User creation failed: {e}")
        return

    # 3. Assessment Phase
    # Determine Emotional Stage (High confidence initially, low competence)
    emotional_stage = AssessmentService.determine_emotional_stage(confidence_level=9, competence_level=2)
    user.current_emotional_stage = emotional_stage
    logger.info(f"User Emotional Stage: {user.current_emotional_stage.value}")

    # Determine Ikigai Quadrant
    ikigai_quadrant = AssessmentService.calculate_ikigai_quadrant(user)
    logger.info(f"Dominant Ikigai Quadrant: {ikigai_quadrant.value}")

    # 4. Recommendation Phase
    try:
        rec = ai_service.generate_recommendation(user)
        
        # 5. Output Results
        print("\n" + "="*40)
        print(f"SPARKLE CAREER REPORT FOR: {user.username.upper()}")
        print("="*40)
        print(f"Status: {user.current_emotional_stage.value}")
        print(f"Alignment: {ikigai_quadrant.value}")
        print("-" * 40)
        print(f"AI Recommendation: {', '.join(rec.recommended_domains)}")
        print(f"Reasoning: {rec.reasoning}")
        print(f"Confidence: {rec.confidence_score * 100}%")
        print("Next Steps:")
        for step in rec.next_steps:
            print(f" - {step}")
        print("="*40 + "\n")
        
    except Exception as e:
        logger.error(f"Error generating recommendation: {e}")

if __name__ == "__main__":
    main()
