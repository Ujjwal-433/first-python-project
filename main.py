from customtkinter import *
import json

class App:
    def __init__(self,root,data):
        self.root = root
        self.data = data
        self.framesholder = CTkScrollableFrame(self.root, 280, 550)
        self.framesholder.place(x = 0, y = 0)
        self.allholder = CTkFrame(self.root, 550, 550)
        self.allholder.place(x=300, y=5)


    def save_text(self,title,content):
      self.count = 0
      if len(self.data) != 0:
        self.count = int(len(self.data))
      new_key = str(self.count)
      self.data[new_key] = {"title" : title , "content" : content}
      with open("data.json" , "w") as f:
        json.dump(self.data, f, indent=3)
      self.addnewbtn.destroy()
      self.frame_creator(new_key)



    def add_items(self):
       self.allholder.destroy()
       self.allholder = CTkFrame(self.root, 550, 550)
       self.allholder.place(x=300, y=5)
       titlebox = CTkEntry(self.allholder, 550, 55, font=("sans-serif", 24), placeholder_text="Enter title")
       titlebox.pack()
       contentbox = CTkTextbox(self.allholder, 550,400, fg_color='#444444',font=("Helvetica", 18) )
       contentbox.pack(pady = 5)
       savebtn = CTkButton(self.allholder,
                           350,
                           72,
                           fg_color= '#0066dd',
                           font= ('sans-serif',32),
                           text= "SAVE NOTE",
                           command= lambda: self.save_text(titlebox.get(), contentbox.get("1.0", "end-1c"))
                          )
       savebtn.pack(pady = 2, padx = 100)


    def handle_items(self,title,content):
        self.allholder.destroy()
        self.allholder = CTkFrame(self.root, 550, 550)
        self.allholder.place(x=300, y=5)
        self.is_changed = False
        titlebox = CTkLabel(self.allholder, 550, 75, text = title, font=("Helvetica", 32, "bold"))
        titlebox.pack()
        contentbox = CTkLabel(self.allholder, 550, 400, text = content, font = ("sans-serif", 18))
        contentbox.pack(pady = 5)


    def delete_json(self,key):
      self.data.pop(key)
      with open("data.json", "w") as f:
        json.dump(self.data, f, indent=3)


    def frame_creator(self, key):
      newframe = CTkFrame(self.framesholder, 280, 50)
      newframe.pack(pady = 1)
      title = self.data[key]["title"]
      content = self.data[key]["content"]
      titlebtn = CTkButton(
        newframe,
        230,
        50,
        text=title,
        command=lambda t=title, c=content: self.handle_items(t, c)
      )
      titlebtn.pack(side=LEFT)
      deletebtn = CTkButton(
      newframe,
      50,
      50,
      fg_color='#bb0000',
      text='X',
      font=("Helvetica", 20, "bold"),
      hover_color='#ff0000',
      command = lambda k=key, fm=newframe: [fm.destroy(),self.delete_json(k)]
      )
      deletebtn.pack(side = RIGHT)
      self.addnewbtn = CTkButton(
          self.framesholder,
          280,
          90,
          text='+',
          fg_color='#00bb00',
          font=("sans serif", 48, "bold"),
          hover_color='#00ff00',
          command = lambda: self.add_items()
          )
      self.addnewbtn.pack(pady = 1)


def main():
    root = CTk()
    root.geometry("850x550")
    root.title("Note for all")
    root.resizable(False,False)
    app = App(root,get_data())
    for key in app.data: 
      app.frame_creator(key)
    root.mainloop()


def get_data():
    try:
      with open("data.json" , "r") as f:  
        data =  json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
       data = {}
       with open("data.json" , "w") as f:
          json.dump(data, f, indent=3)
    return data


if __name__ == "__main__":
  main()