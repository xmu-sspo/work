/*热度分析图*/
(function(){
	var myChart = echarts.init(document.getElementById("main"));
	
	var option = {
		    title : {
		        text: '三天新闻热度变化',
		        subtext: '2018/11/22-2018/11/24'
		    },
		    tooltip : {
		        trigger: 'axis'
		    },
		    legend: {
		        data:['习近平考察深圳广州','日本首相安倍今日起访华']
		    },
		    toolbox: {
		        show : true,
		        feature : {
		            mark : {show: true},
		            dataView : {show: true, readOnly: false},
		            magicType : {show: true, type: ['line', 'bar']},
		            restore : {show: true},
		            saveAsImage : {show: true}
		        }
		    },
		    calculable : true,
		    xAxis : [
		        {
		            type : 'category',
		            boundaryGap : false,
		            data : ['208/11/22','2018/11/23','2018/11/24']//['周一','周二','周三','周四','周五','周六','周日']
		        }
		    ],
		    yAxis : [
		        {
		            type : 'value',
		            axisLabel : {
		                formatter: '{value} '
		            }
		        }
		    ],
		    series : [
		        {
		            name:'习近平考察深圳广州',
		            type:'line',
		            data:[10, 21, 15],
		            markPoint : {
		                data : [
		                    {type : 'max', name: '最大值'},
		                    {type : 'min', name: '最小值'}
		                ]
		            },
		            markLine : {
		                data : [
		                    {type : 'average', name: '平均值'}
		                ]
		            }
		        },
		        {
		            name:'日本首相安倍今日起访华',
		            type:'line',
		            data:[1, 0, 2],
		            markPoint : {
		                data : [
		                    {name : '周最低', value : 0, xAxis: 1, yAxis: -1.5}
		                ]
		            },
		            markLine : {
		                data : [
		                    {type : 'average', name : '平均值'}
		                ]
		            }
		        }
		    ]
		};    
	myChart.setOption(option);
	
})();