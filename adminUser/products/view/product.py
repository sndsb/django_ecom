from django.shortcuts import render,redirect
from django.contrib import messages
from adminUser.products.model.product import Product
from django.http import JsonResponse
from django.db.models import Q


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
    search_arr = request.GET.get('search', {})

    columnIndex = int(columnIndex_arr[0]['column']) if columnIndex_arr else 0
    columnName = columnName_arr[columnIndex]['data'] if columnName_arr else 'id'
    columnSortOrder = order_arr[0]['dir'] if order_arr else 'asc'
    searchValue = search_arr.get('value', '')

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

        data_arr.append({
            "id": i,
            "name": f"<a class='text-info' href='#'>{record.name}</a>",
            "slug": record.slug,
            "sku": record.sku,
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
