import graphene
from graphene_django import DjangoObjectType
from home.models import Quiz


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = '__all__'


class Query(graphene.ObjectType):
    quizzes = graphene.List(QuizType)
    singele_quiz = graphene.Field(QuizType, id=graphene.Int())

    def resolve_quizzes(self, info, **kwargs):
        return Quiz.objects.all()
    
    def resolve_singele_quiz(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Quiz.objects.get(pk=id)
        return None


class QuizMutationCreate(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
    
    quiz = graphene.Field(QuizType)

    @classmethod
    def mutate(cls, root, info, name, description):
        quiz = Quiz(name=name, description=description)
        quiz.save()
        return QuizMutationCreate(quiz=quiz)

class QuizMutationUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)
    
    quiz = graphene.Field(QuizType)

    @classmethod
    def mutate(cls, root, info, id, name, description):
        quiz = Quiz.objects.get(pk=id)
        quiz.name = name
        quiz.description = description
        quiz.save()
        return QuizMutationUpdate(quiz=quiz)
class QuizMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    
    quiz = graphene.Field(QuizType)

    @classmethod
    def mutate(cls, root, info, id):
        quiz = Quiz.objects.get(pk=id)
        quiz.delete()
        return

class Mutation(graphene.ObjectType):
    create_quiz = QuizMutationCreate.Field()
    update_quiz = QuizMutationUpdate.Field()
    delete_quiz = QuizMutationDelete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)