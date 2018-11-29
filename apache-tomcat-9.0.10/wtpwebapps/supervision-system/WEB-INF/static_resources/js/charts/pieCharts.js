(function(){
	var pie = echarts.init(document.getElementById("pie"));
	var option2 = {
			title : {
		        text: '"国产原创综艺《一本好书》评分9.3，我实名吹爆！"',
		        subtext: '话题发布平台统计',
		        x:'center'
		    },
		    tooltip : {
		        trigger: 'item',
		        formatter: "{a} <br/>{b} : {c} ({d}%)"
		    },
		    legend: {
		        orient : 'vertical',
		        x : 'left',
		        data:['新浪网','环球网','观察者网','新京报']
		    },
		    toolbox: {
		        show : true,
		        feature : {
		            mark : {show: true},
		            dataView : {show: true, readOnly: false},
		            magicType : {
		                show: true, 
		                type: ['pie', 'funnel'],
		                option: {
		                    funnel: {
		                        x: '25%',
		                        width: '50%',
		                        funnelAlign: 'left',
		                        max: 1548
		                    }
		                }
		            },
		            restore : {show: true},
		            saveAsImage : {show: true}
		        }
		    },
		    calculable : true,
		    series : [
		        {
		            name:'新闻来源',
		            type:'pie',
		            radius : '55%',
		            center: ['50%', '60%'],
		            data:[
		                {value:72, name:'新浪网'},
		                {value:46, name:'环球网'},
		                {value:34, name:'观察者网'},
		                {value:4, name:'新京报'}
		            ]
		        }
		    ]
		};
		                    
	pie.setOption(option2);
})();