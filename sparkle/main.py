#!filepath main.py
from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List

from models import (
    UserProfile, RecommendationResponse, CourseResponse, 
    ProgressUpdateRequest, EmotionalStage
)
from services import (
    DomainRepository, CourseRepository, AssessmentService, ProgressService
)

app = FastAPI(title="Sparkle API")

# Dependency Injection (Singleton for demo)
domain_repo = DomainRepository()
course_repo = CourseRepository()
progress_service = ProgressService()

# Mock User DB
MOCK_USER = UserProfile(
    id=UUID("12345678-1234-5678-1234-567812345678"),
    username="Dotun",
    email="dotun@example.com",
    ikigai_inputs={"love": 9, "good_at": 8, "world_needs": 7, "paid_for": 8}
)

@app.get("/recommendations/{user_id}", response_model=RecommendationResponse)
async def get_recommendations(user_id: UUID):
    """
    Generates the personalized path and MERGES it with the user's
    current progress and emotional state into a single response.
    """
    # 1. Logic: Determine Domain based on Ikigai
    quadrant = AssessmentService.ikigai_quadrant(MOCK_USER)
    
    # 2. Logic: Fetch Courses (Simplified for demo: fetching all)
    all_courses = []
    for domain in domain_repo.all():
        for sub in domain.subdomains:
            all_courses.extend(course_repo.by_subdomain(sub.name))
            
    # 3. MERGE: Create the Response Objects
    response_courses = []
    
    for course in all_courses:
        # Get dynamic progress
        current_percent = progress_service.get_progress(user_id, course.id)
        # Calculate dynamic emotion
        current_emotion = AssessmentService.predict_emotional_stage(current_percent)
        
        # Build the DTO
        response_courses.append(CourseResponse(
            id=course.id,
            title=course.title,
            platform=course.platform,
            url=course.url,
            level=course.level,
            duration_hours=course.duration_hours,
            # Merged fields
            emotional_stage=current_emotion,
            progress=current_percent
        ))
    
    return RecommendationResponse(
        user_id=user_id,
        domains=[d.name for d in domain_repo.all()],
        reasoning=f"Based on your strength in {quadrant.value}, we suggest these paths.",
        confidence_score=0.92,
        courses=response_courses
    )

@app.post("/progress", response_model=EmotionalStage)
async def update_progress(data: ProgressUpdateRequest):
    """Updates progress and returns the new Emotional Stage immediately."""
    new_stage = progress_service.update_progress(
        data.user_id, data.course_id, data.progress
    )
    return new_stage

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
