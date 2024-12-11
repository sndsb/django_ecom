// ajax call
	function ajaxPost(url,data,callback_url,method,$form){
		 $.ajax({
			 url:url,
			 method:method,
			 data:data,
			 contentType: false,
			processData: false,
			headers: {
                'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
			},
			 success:function (responseData){
				 if(responseData.response){
					 // toastr.success(responseData.msg)
                         location.replace(callback_url)
				 }else{
					   displayErrors($form, responseData.errors);  displayErrors($form, responseData.errors);
				 }
			 }
		 })
	}

	  function displayErrors($form, errors) {
            $.each(errors, function(field, messages) {
                let $field = $form.find('[name="' + field + '"]');

                $field.removeClass('is-invalid');
                $field.siblings('.error-message').remove();

                if ($field.length) {
                    $field.addClass('is-invalid');
                    $field.after('<div class="error-message text-danger small">' + messages.join('<br>') + '</div>');
                }
            });
        }
