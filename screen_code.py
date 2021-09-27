screen_helper = """
Screen:

    BoxLayout:
        orientation : 'vertical'

        MDToolbar:
            title : 'BMH App'
            left_action_items: [["menu", lambda x: nav_drawer. set_state()]]
            #right_action_items: [["clock",lambda x: app.clock_def()]]
            right_action_items: [["dots-vertical", lambda x: app.callback_1()],["clock", lambda x: app.clock_def()]]
            elevation : 8 

        MDLabel:
            text: 'Welcome to BMH App'
            halign: 'center'
              
        MDTextField:
            text:"enter a password"
            #password:True
            halign:"center"
            #pos_hint:{"center_x": 0.5, "center_y": 0.8}
            font_size :20 
       
            
            
        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["coffee",lambda x: idcoffee.set_state()]]# app.coffee_def()]]
                type: 'bottom' 
                title : 'Help '
                icon:'logout'
                #icon_color: 0, 1, 0, 1
                mode: 'end'                  
                on_action_button : app.logout_def()
                
           

    MDNavigationLayout:
        
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp' 
                padding: '8dp'

                Image:
                    size_hint: None, None
                    size: "56dp", "56dp"
                    source: 'myphoto.jpg'

                MDLabel:
                    text: '    BOURAGHDA MOHAMED EL HADI'
                    font_style: 'Subtitle2'
                    size_hint_y : None
                    height : self.texture_size[1]

                MDLabel:
                    text: '    bmhwin@gmail.com'
                    font_style: 'Caption'
                    size_hint_y : None
                    height : self.texture_size[1]

                ScrollView:
                    MDList:
                        MDList:
                        OneLineIconListItem:
                            on_release: idProfile.set_state() 
                            text: 'Profile'
                            IconLeftWidget : 
                                icon: 'face-profile-woman'
                     
                        OneLineIconListItem:
                            on_release:  
                            text: 'My files'
                            IconLeftWidget : 
                                icon: 'folder'
                        OneLineIconListItem:
                            on_release:  
                            text: 'Shared with me'
                            IconLeftWidget : 
                                icon: 'account-multiple'
                        OneLineIconListItem:
                            on_release: 
                            text: 'Starred'
                            IconLeftWidget : 
                                icon: 'star'                                  
                        
                        OneLineIconListItem:
                            on_release:  
                            text: 'Recent'
                            IconLeftWidget : 
                                icon: 'history'
                       
                        OneLineIconListItem:
                            on_release: print("Upload") 
                            text: 'Upload'
                            IconLeftWidget : 
                                icon: 'upload'                             
        
    MDNavigationLayout: # Profile
        
        MDNavigationDrawer:
            id: idProfile 

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp' 
                padding: '8dp'
                
                Image:
                    source: 'myphoto.jpg'
               
                MDLabel:
                    text: '    BOURAGHDA MOHAMED EL HADI'
                    font_style: 'Subtitle2'
                    size_hint_y : None
                    height : self.texture_size[1]

                MDLabel:
                    text: '    bmhwin@gmail.com'
                    font_style: 'Caption'
                    size_hint_y : None
                    height : self.texture_size[1]
                    
                MDFlatButton:
                    text: "back"
                    theme_text_color: "Custom"
                    text_color: 0, 0, 1, 1       
                    on_press: print('back')
                    #on_release:nav_drawer.set_state() 

    MDNavigationLayout: # coffee
        
        MDNavigationDrawer:
            id: idcoffee

            BoxLayout:
              
                orientation: 'vertical'
                spacing: '8dp' 
                padding: '8dp'
                
                Image:
                    source: 'CupCoffee.jpg'  
                 
                MDLabel:
                    text: '   Coffee Arabisca'
                    font_style: 'Subtitle2'                  

                MDLabel:
                    text: '    05 56 24 14 21'
                    font_style: 'Caption'
            
                    
                   


"""