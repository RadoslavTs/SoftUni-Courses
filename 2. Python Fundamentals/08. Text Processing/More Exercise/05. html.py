article_title = input()
content_article = input()
comment = input()
comment_list = []
while comment != "end of comments":
    comment_list.append(comment)
    comment = input()
print("<h1>")
print(f"    {article_title}")
print("</h1>")
print("<article>")
print(f"    {content_article}")
print("</article>")
for commenting in comment_list:
    print("<div>")
    print(f"    {commenting}")
    print("</div>")
