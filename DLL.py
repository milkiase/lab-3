class Music:
    def __init__(self, id, title):
        self.id= id
        self.title = title
        self.next = None
        self.prev = None
class MusicList:
    def __init__(self):
        self.head = None
    def append(self,id,title):
        new_music = Music(id,title)
        if self.head is None:
            self.head=new_music
            new_music.next=self.head
            new_music.prev=new_music
        else:
            last_node = self.head
            while last_node.next is not self.head:
                last_node = last_node.next
            new_music.prev=last_node
            new_music.next=self.head
            last_node.next=new_music
            self.head.prev = new_music
            del last_node
    def delete(self,title):
        temp = self.head
        if temp.title is title:
            if temp.next is temp:
                self.head=None
                return
            else:
                nxt=temp.next
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                self.head=nxt
                del temp
        else:
            while True:
                if temp.title is  title:
                    nxt=temp.next
                    prev=temp.prev
                    nxt.prev=prev
                    prev.next=nxt
                    del temp
                    break

                if temp.next is self.head:
                    print("the song doesn't exist")
                    break
                temp = temp.next
    def upload_multiple(self,ids,titles):
        i=0
        while i<len(ids):
            self.append(ids[i],titles[i])
            i+=1

    def get(self,title):
        print(f"music '{title}' is found to play press 'P'")
        inpt = input(":")
        if inpt in "pP":
            print(f"music '{title}' is now playing")
    def search_music(self,title):
        temp = self.head
        if temp.title is title:
            self.get(title)
        else:
            temp=temp.next
            while temp is not self.head:
                if temp.title is title:
                    self.get(title)
                    return
                temp=temp.next
        print(f"the music {title} is not found")
    def print_all(self):
        temp = self.head
        while True:
            print(F"{temp.title} : {temp.id}")
            if temp.next is  self.head:
                break
            temp = temp.next
l1=MusicList()
l1.append(527,"track 1")
l1.append(538,"track 2")
l1.append(619,"track 3")
l1.print_all()
print ("----------")
l1.delete("track 3")
ID = [432,564,906]
title=["track 4","track 5", "track 6"]
l1.upload_multiple(ID,title)

l1.print_all()
l1.search_music("track 4")
