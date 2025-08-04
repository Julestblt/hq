"""
Test fixtures and sample HTML for testing
"""

SIMPLE_HTML = """
<html>
<head>
    <title>Test Page</title>
    <meta name="description" content="A test page">
</head>
<body>
    <h1>Welcome</h1>
    <div class="content">
        <p>First paragraph</p>
        <p>Second paragraph</p>
        <a href="https://example.com">Example Link</a>
    </div>
    <div id="sidebar">
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </div>
    <form>
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

COMPLEX_HTML = """
<html>
<head>
    <title>Complex Page</title>
</head>
<body>
    <nav id="main-nav">
        <ul class="nav-list">
            <li><a href="/home" class="nav-link">Home</a></li>
            <li><a href="/about" class="nav-link">About</a></li>
            <li><a href="/contact" class="nav-link">Contact</a></li>
        </ul>
    </nav>
    
    <main>
        <article class="post" data-id="1">
            <h2>First Article</h2>
            <p class="excerpt">This is the first article excerpt.</p>
            <div class="meta">
                <span class="author">John Doe</span>
                <time datetime="2024-01-01">January 1, 2024</time>
            </div>
        </article>
        
        <article class="post" data-id="2">
            <h2>Second Article</h2>
            <p class="excerpt">This is the second article excerpt.</p>
            <div class="meta">
                <span class="author">Jane Smith</span>
                <time datetime="2024-01-02">January 2, 2024</time>
            </div>
        </article>
    </main>
    
    <aside>
        <div class="widget">
            <h3>Recent Posts</h3>
            <ul>
                <li><a href="/post/1">Post 1</a></li>
                <li><a href="/post/2">Post 2</a></li>
            </ul>
        </div>
    </aside>
</body>
</html>
"""

MALFORMED_HTML = """
<html>
<head>
    <title>Malformed Page
</head>
<body>
    <div class="content">
        <p>Paragraph without closing tag
        <a href="example.com">Link without protocol</a>
    </div>
    <img src="image.jpg" alt="Test image"
</body>
"""
