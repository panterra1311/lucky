from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView  # импортируем необходимые дженерики
from django.core.paginator import Paginator
from datetime import datetime

from .models import Category
from .filters import ProductFilter
from .forms import ProductForm
from django.shortcuts import render
from django.views import View
from .models import Product



class Products(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'flatpages/product_list.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    paginate_by = 10 # поставим постраничный вывод в один элемент
    form_class = ProductForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_filter(self):
        return ProductFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }

    # из списка на главной странице уберём всё лишнее
    def get_context_data1(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter()
        context['date_time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['categories'] = Category.objects.all()
        context['form'] = ProductForm()
        context['date_product_create'] = datetime.utcnow()
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)



class ProductDetailView(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'flatpages/product_detail.html'
    context_object_name = 'product'  # название объекта. в нём будет
    queryset = Product.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class ProductCreateView(CreateView):
    model = Product
    template_name = 'flatpages/product_create.html'
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'flatpages/product_create.html'
    form_class = ProductForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'flatpages/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'


