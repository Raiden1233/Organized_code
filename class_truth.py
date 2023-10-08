import truth as t
import Dare as d
import discord

def embed(titel, description):
   em = discord.Embed(title =titel, description = description)
   return em
class Truth(discord.ui.View):
   def __init__(self, icon_url,name):
      super().__init__(timeout = None)
      
    #   self.is_persistent()
      self.icon_url = icon_url
      self.name = name

   @discord.ui.button(label= 'Truth',custom_id=' button1', style = discord.ButtonStyle.green)
   async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
    

    # button.disabled = True
    em = embed('Question',t.t_question())
    em.set_author(name=f'requested by {self.name}',
                  icon_url= self.icon_url)
    

    await interaction.response.edit_message(view = None)
    await interaction.followup.send(embed = em, view = Truth(self.icon_url, self.name))



   @discord.ui.button(label= 'Dare',custom_id=' button2', style = discord.ButtonStyle.red)
   async def button2(self, interaction: discord.Interaction, button: discord.ui.Button):
    
    em = discord.Embed(title ='Dare', description = d.d_dare()) 
    em.set_author(name=f'requested by {self.name}',
                  icon_url= self.icon_url)
    

    await interaction.response.edit_message(view = None)
    await interaction.followup.send(embed = em, view = Truth(self.icon_url, self.name))

