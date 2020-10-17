from django.db.models import Q
from rest_framework import mixins
from rest_framework import generics
from webapp.models import Inscription
from webapp.serializers import InscriptionSerializer


class InscriptionList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class InscriptionDetail(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class InscriptionUserId(generics.ListAPIView):

    serializer_class = InscriptionSerializer

    def get_queryset(self, *args, **kwargs):
        list1=Inscription.objects.all()
        query=self.request.GET.get("id_usuario")
        print(query)
        if query:
            list1=list1.filter(
                Q(id_usuario__exact=query)
            )
        return list1


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class InscriptionUserIdAndCourseId(generics.ListAPIView):
    serializer_class = InscriptionSerializer

    def get_queryset(self, *args, **kwargs):
        list1 = Inscription.objects.all()
        q, q2 = self.request.GET.get("id_usuario"), self.request.GET.get("id_curso")
        print(q)
        print(q2)
        if q and q2:
            list1 = list1.filter(
                Q(id_usuario__exact=q),
                Q(id_curso__exact=q2)
            )
        return list1

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
