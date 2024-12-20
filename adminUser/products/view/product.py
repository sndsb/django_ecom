from django.shortcuts import render,redirect
from django.contrib import messages
from adminUser.products.model.products import Product, Category, Attribute, ProductAttribute
from django.http import JsonResponse
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import IntegrityError


def index(request):

    return render(request,'products/index.html',{})

def list(request):

    # Get request parameters
    draw = request.GET.get('draw')
    start = int(request.GET.get('start', 0))
    rowperpage = int(request.GET.get('length', 10))

    # Sorting details
    columnIndex_arr = request.GET.getlist('order[]')
    columnName_arr = request.GET.getlist('columns[]')
    order_arr = request.GET.getlist('order[]')
    # search_arr = request.GET.get('search', {})

    columnIndex = int(columnIndex_arr[0]['column']) if columnIndex_arr else 0
    columnName = columnName_arr[columnIndex]['data'] if columnName_arr else 'id'
    columnSortOrder = order_arr[0]['dir'] if order_arr else 'asc'
    # searchValue = search_arr.get('value', '')
    searchValue = request.GET['search[value]']

    # Build the query with search filters
    query = Product.objects.all()

    if searchValue:
        query = query.filter(
            Q(name__icontains=searchValue) |
            Q(slug__icontains=searchValue) |
            Q(sku__icontains=searchValue)
        )
        

    # Get total count (before applying pagination)
    totalRecords = query.count()

    # Sorting logic
    if columnSortOrder == 'asc':
        query = query.order_by(columnName)
    else:
        query = query.order_by('-' + columnName)

    # Pagination
    queryset = query[start:start + rowperpage]

    # Prepare the data for response
    data_arr = []
    i = start + 1
    for record in queryset:
        actionBtn = '''
            <div class="dropdown">
                <button type="button" class="btn btn-sm btn-primary dropdown-toggle" data-toggle="dropdown">
                    <i class="fe fe-calendar mr-2"></i>Action
                </button>
                <div class="dropdown-menu">
                    <a class="dropdown-item text-info" href="#">Edit</a>
                    <a class="dropdown-item text-black" href="#">Game Details</a>
                    <a class="dropdown-item text-primary" href="#">Game Prize</a>
                </div>
            </div>
        '''
        image_tag = f"<img src='{record.image.url}' alt='{record.name}' style='width: 50px; height: 50px;' />" if record.image else "No Image"

        data_arr.append({
            "id": i,
            "name": f"<a class='text-info' href='#'>{record.name}</a>",
            "slug": record.slug,
            "sku": record.sku,
            'image':image_tag,
            "action": actionBtn
        })
        i += 1

    # Return the response data
    response = {
        "draw": int(draw),
        "iTotalRecords": totalRecords,
        "iTotalDisplayRecords": totalRecords,  # Assuming no filtering is applied to total count
        "aaData": data_arr
    }

    return JsonResponse(response)

def add(request):
    categories = Category.objects.all()
    attributes = Attribute.objects.all()
    return render(request,'products/add.html',{'categories':categories,'attributes':attributes})

MAX_IMAGE_SIZE_MB = 3

@login_required
@require_POST
def save(request):
    pass
    
    try:
        name = request.POST.get('name')
        description = request.POST.get('description')
        sku = request.POST.get('sku')
        category_id = request.POST.get('category_id')
        image = request.FILES.get('image')
        
         # Image size validation
        print('sku : ', sku)
        if image :
          
            if image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
               
                raise ValidationError({'image': f"Image size should not exceed {MAX_IMAGE_SIZE_MB} MB."})
             
        else:
            pass
            
        
        product = Product(
            name=name,
            description=description,
            sku=sku,
            category_id=category_id,
            image=image
        )

        product.full_clean()

        product.save()

       # Extract attribute data
        attribute_ids = request.POST.getlist('attribute_id[]')
        attribute_values = request.POST.getlist('attribute_value[]')
        attribute_price = request.POST.getlist('attr_price[]')
        attr_stocks = request.POST.getlist('attr_stock[]')

        # extract non attribute data
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        if(price):
            produWithoutAttribute = ProductAttribute(
                product_id=product.id,
                price=price,
                stock=stock,
            )
            produWithoutAttribute.full_clean()

            produWithoutAttribute.save()
        else:
            for i in range(len(attribute_ids)):

                productattribute = ProductAttribute(
                    product_id=product.id,
                    attribute_id=attribute_ids[i],
                    attribute_value=attribute_values[i],
                    price = attribute_price[i],
                    stock=attr_stocks[i]
                )

                productattribute.full_clean()

                productattribute.save()


        
        response = {
            'response': True,
            'msg': "Product Added Successfully",
            'result': "",
        }

    except IntegrityError:
      
        raise ValidationError({'sku': "SKU should be unique."})

    except ValidationError as error:
     
        response = {
            'response': False,
            'msg': "Validation error occurred.",
            'result' : "",
            'errors': error.message_dict,
        }

    return JsonResponse(response)
