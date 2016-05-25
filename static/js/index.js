// all js used in index.html

$(function () {

	$.ajax({
		type:'GET',
	url:'/api/getvari/',
	contentType: "application/json",
	success:function(result){
		data = result;
	},
	error:function(e){
		alert('!!!\n' + JSON.stringify(e));
	}
	});

	// Slideshow 4
	$("#slider3").responsiveSlides({
		auto: false,
		pager: true,
		nav: false,
		namespace: "callbacks",
		before: function () {
			$('.events').append("<li>before event fired.</li>");
		},
		after: function () {
			$('.events').append("<li>after event fired.</li>");
		}
	});

	$(".add").click(function() {
		n = parseInt($(this).prev().val());
		if(isNaN(n) || n<0) n=1;
		else n=n+1;
		$(this).prev().val(n);
		unit = $(this).siblings(".unit").val();
		$(this).siblings(".price").text(n*unit);
	});

	$(".min").click(function() {
		n = parseInt($(this).next().val());
		if(isNaN(n) || n<1) n=0;
		else n=n-1;
		$(this).next().val(n);
		unit = $(this).siblings(".unit").val();
		$(this).siblings(".price").text(n*unit);
	});

	$(".prev").click(function() {
		$(".callbacks_here").prev().children().click();
	});

	$(".next").click(function() {
		$(".callbacks_here").next().children().click();
	});

	$(".variopt").change(function() {
		var v = data.data[$(this).val() - 1];

		$(this).parent().siblings(".cal").val(v['cal']);
		$(this).parent().siblings(".pro").val(v['pro']);
		$(this).parent().siblings(".fat").val(v['fat']);
		$(this).parent().siblings(".car").val(v['car']);

		$(this).parent().siblings(".image-container").find("td.cal").html(v['cal']);
		$(this).parent().siblings(".image-container").find("td.pro").html(v['pro']);
		$(this).parent().siblings(".image-container").find("td.fat").html(v['fat']);
		$(this).parent().siblings(".image-container").find("td.car").html(v['car']);

	});

	$(".confirm").click(function() {
		// calculate total bill
		var sum = 0;
		$(".price").each(function() {
			sum += parseInt($(this).text());
		});
		if (sum <= 0) {
			alert("不许胡闹哟～");
			return false;
		}

		// calculate details
		var order = '\n';
		var postdata = new Object;
		postdata['cal'] = 0;
		postdata['pro'] = 0;
		postdata['fat'] = 0;
		postdata['car'] = 0;

		$(".cate-id").each(function(){
			var id = $(this).html();
			postdata[id] = new Object;
			postdata[id]['name'] = $(this).siblings(".cate-name").html();
			postdata[id]['item'] = new Array;
		})
		$(".item-name").each(function(){
			var num = $(this).parent().siblings(".text-box").val();
			if (num > 0) {
				var id = $(this).parents(".testimonials-grid").children(".cate-id").html();
				var name = $(this).html();
				var sid = $(this).parent().siblings(".text-box").attr("name");
				var unit = $(this).parent().siblings(".unit").val();
				var tmp = new Object;
				tmp['sid'] = sid;
				tmp['name'] = name;
				tmp['num'] = parseInt(num);
				tmp['unit'] = parseInt(unit);
				postdata[id]['item'].push(tmp);
				postdata['cal'] += num * $(this).parent().siblings(".cal").val();
				postdata['pro'] += num * $(this).parent().siblings(".pro").val();
				postdata['fat'] += num * $(this).parent().siblings(".fat").val();
				postdata['car'] += num * $(this).parent().siblings(".car").val();
			}
		});
		postdata['price'] = sum;
		var prefix = '你忘了点 '
			var suffix = ', 确定继续么？';
		var mid = '';
		$(".cate-id").each(function(){
			var id = $(this).html();
			if (postdata[id]['item'].length == 0)
			mid += postdata[id]['name'] + ' ';
		})
		if (mid.length > 0) {
			<!--alert(JSON.stringify(postdata))-->
				if (!confirm(prefix + mid + suffix)) {
					return false;
				}
		}
		$.ajax({
			type:'POST',
			url:'/api/neworder/',
			data:JSON.stringify(postdata),
			contentType: "application/json",
			success:function(result){
				$(testimonials).html(result);
			},
			error:function(e){
				alert('!!!\n' + JSON.stringify(e));
			}
		});

	});

});

