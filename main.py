import Service.News_Service as news_service

def main():
    print("=====Welcome TO Console Based Newsd Application System=====")
    print("a) Fetch Article")
    print("b) Generate Summary")
    print("c) View Article Titles")
    print("d) Delete Article")
    print("e) Exit")

    choice = input("Choice : ")
    if choice == 'a':
        news_service.fetch_articles()
    elif choice == 'b':
        news_service.Summary()
    elif choice == 'c':
        news_service.View_Article_Titles()
    elif choice == 'd':
        news_service.Delete_Article()
    elif choice == 'e':
        return news_service.Exit()
    else:
        print("Invalid Choice!! Please Try Again!!")
    return True

while True:
    if not main():
        break
    