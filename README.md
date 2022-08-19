<div id="totop">
        <a href="javascript:;" id="btn">顶部</a>
</div>

<body>
<script type="text/javascript">
        window.onload = function () {
            // 1.找到页面中的按钮
            var totop = document.getElementById("btn");
            totop.style.display ="none";
            var timer = null;
 
            // 2. 给按钮绑定点击事件
            totop.onclick =function () {
                // 周期性定时
                timer = setInterval(function () {
                    // 3.获取滚动条距离浏览器顶端的距离
                    var backTop = document.documentElement.scrollTop || 
                    document.body.scrollTop;
 
                    // 越滚越慢
                    speedTop =backTop/5;
                    document.documentElement.scrollTop=backTop-speedTop;
                    if(backTop==0){
                        clearInterval(timer);
                    }
                },30)
            }
            // 设置临界值
            var pageHeight =700;
            window.onscroll =function () {
                var backTop = document.documentElement.scrollTop || 
                document.body.scrollTop;
                if(backTop>pageHeight){
                    totop.style.display="block";
                }else{
                    totop.style.display="none";
                }
 
            }
        }
 
    </script>
    </body>

<h1 align="center">Hi,</h1>

# MyWebsites

- [SpanishLearning2022](https://liu-xnd.github.io/SpanishLearning2022)

- [Bioinfo&Genomics2022](https://github.com/LIU-Xnd/LIU-Xnd.github.io/blob/main/_bioinformatics/notes_bio_gen.md)
