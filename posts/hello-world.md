---
title: "첫 번째 포스트"
date: "2026-05-19"
summary: "블로그를 시작합니다. Flask와 Vercel로 만든 첫 글입니다."
tags: ["시작", "Flask", "블로그"]
---

## 안녕하세요!

이 블로그는 **Flask**와 **Vercel**로 만들어졌습니다.

### 마크다운을 지원합니다

- 목록 작성 가능
- **굵게**, *기울임* 지원
- 코드 블록도 됩니다

```python
def hello():
    return "Hello, Blog!"


---

## 📄 `templates/base.html`

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{% block title %}My Blog{% endblock %}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
  <header>
    <nav>
      <a href="/" class="logo">✦ My Blog</a>
      <div class="nav-links">
        <a href="/">글 목록</a>
        <a href="/about">소개</a>
      </div>
    </nav>
  </header>

  <main>
    {% block content %}{% endblock %}
  </main>

  <footer>
    <p>© 2026 My Blog · Flask + Vercel</p>
  </footer>
</body>
</html>
