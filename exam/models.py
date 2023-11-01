from django.db import models


# Create your models here.

# models.py
class Chapter(models.Model):  # 章节
    content = models.TextField()  # 章节名

    def __str__(self):
        return self.content


class Unit(models.Model):  # 单元
    content = models.TextField()  # 单元名
    unit_id = models.FloatField()  # 单元编号  2.1 2.2这种
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Knowledge_point(models.Model):  # 知识点
    content = models.TextField()  # 知识点名称
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)  # 属于哪个单元

    def __str__(self):
        return self.content


class Question(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    knowledge_point = models.ForeignKey(Knowledge_point, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content
