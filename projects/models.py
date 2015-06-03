from django.db import models
from django.utils import timezone

class Project(models.Model):
    """Project is container for sprints"""
    project_name = models.CharField(max_length = 200)
    customer_name = models.CharField(max_length = 200)
    created_at = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.project_name

class Sprint(models.Model):
    """Sprint is repeatable period and contains some stories/tasks"""
    sprint_description = models.TextField('')
    project = models.ForeignKey(Project)
    def __unicode__(self):
        return self.sprint_description

class Stakeholder(models.Model):
    """Stakeholder of project can be admin, HRM, Employee, user, guest, etc.."""
    stakeholder_name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)
    def __unicode__(self):
        return self.stakeholder_name

class Story(models.Model):
    """Story is short of user story and it represents a small task"""
    story_name = models.CharField(max_length=200)    
    story_goal = models.CharField(max_length=200)    
    story_function = models.CharField(max_length=200)    
    stakeholder = models.ForeignKey(Stakeholder)
    sprint = models.ForeignKey(Sprint)
    def __unicode__(self):
        return "As %s in order to %s I should be able to %s" % (self.stakeholder, self.story_goal, self.story_function)


