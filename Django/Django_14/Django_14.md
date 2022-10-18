## A ONE-TO-MANY RELATIONSHIP

### ROB(관계형 데이터베이스) 

- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- 주문 서비스 데이터베이스: 고객 테이블, 주문 테이블 

- 1:1
  - One-to-one relationships
  - 한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우

- 1:N
  - One-to-many relationships
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관려된 경우
  - 기준 테이블에 따라 (1:N, One-to-many relationships)

- M:N
  - Many-to-many relationships
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
  - 양쪽 모두에서 1:N 관계를 가짐



### Foreign Key

- 키를 사용하여 부모 테이블의 유일한 값을 참조
  - 참조 무결성: 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성

- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함

- A one-to-many relationship을 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 데이터베이스의 와래 키 속성을 담당
- 2개의 필수 위치 인자가 필요 
  - 참조하는 model class
  - On_delete 옵션



### 모델 관계 설정

- 게시판의 게시글과 1:N 관계를 나타낼 수 있는 댓글 구현
  - 1:N 관계에서 댓글을 담당할 Article 모델은 1, comment 모델은 N이 될 것
    - 게시글은 댓글을 0개 이상 가진다
    - 게시글(1)은 여러 개의 댓글(N)을 가진다
    - 게시글(1)은 댓글을 가지지 않을 수도 있다
    - 댓글은 반드시 하나의 게시글에 속한다

 

## On_delete

- 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의
- 데이터 무결성을 위해서 매우 중요한 설정
- On_delete 옵션 값
  - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 떄 이를 참조하는 객체도 삭제

```python
# article/models.py

class Comment(models.Modle):
  article = models.ForegnKey(Article, on_delete.CASCADE)
  content = models.CharField(max_length=80)
  created_at = models.DataTimeField(auto_now_add=True)
  created_at = models.DataTimeField(auto_now=True)
  
  def __str__(self):
    ruturn self.content
```

```python
# articles/forms.py

from .models import Article, Comment

class CommentForm(forms.ModleForm):
  class Meta:
    model = Comment
    fields = "__all__"
```

````python
# articles/views.py

from .forms import ArticlesForm, CommentForm

def detail(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm()
  comments = article.comment_set.all()
  context = {
    'article': article,
    'comment_form': comment_form,
    'comments': comments,
  }
  return render(request, 'articles/detail.html', context)
````

````python
# articles/detail.html

{% extends 'base.html' %}
{% block content %}
...
<a href="{% url 'articles:index' %}">back</a>
<hr>
<h4>댓글 목록</h4>
<ul>
	{% for comment in comments %}
  	<li>{{ comment.content }}</li>
  {% endfor %}
</ul>
...
{% endlock content %}
````

````python
# articles/views.py

def comments_create(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid()
  		# 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    	# 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용
  		comment = comment_form.save(commit=False)
    	comment.article = article
      comment.save()
  return render(request, 'articles/detail.html', article.pk)
````





## 관계 모델 참조

### 역참조

- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조
- 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
- 1:N 관계에서는 1이 N을 참조

````python
article.comment_set.method()
````

- Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저 

- Article.comment 형식으로 댓글 객체를 참조 할 수 없음

  - 대신 Django가 역참조 할 수 있는 comment_set manage를 자동ㄷ으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음 

    **1:N 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set" 이름 규칙으로 만들어짐**

- 참조 상황(Comment -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스 변수이기 떄문에 Comment.article 형태로 작성 가능 