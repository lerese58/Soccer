from Pusher import domain, utils

if __name__ == '__main__':
    if utils.download_xml() == 200:  # OK
        posts = utils.get_tagged_posts()
        domain.insert_new_posts(posts)
    else:
        print("Error loading file")
