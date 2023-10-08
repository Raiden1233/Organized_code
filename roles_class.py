import discord


class Roles(discord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
  @discord.ui.button(label = "📢", custom_id = "Announcement", style = discord.ButtonStyle.secondary)
  async def button1(self, interaction, button):
    role = 1129944467349184523 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)

  
  @discord.ui.button(label = "♂️", custom_id = "Male", style = discord.ButtonStyle.secondary)
  async def button2(self, interaction, button):
    role = 1130613893463543809  #put your role id here
    user = interaction.user 
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)
  
  
  @discord.ui.button(label = "♀️", custom_id = "Female", style = discord.ButtonStyle.secondary)
  async def button3(self, interaction, button):
    role = 1130613987134939136 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "⚧️", custom_id = "Others", style = discord.ButtonStyle.secondary)
  async def button4(self, interaction, button):
    role = 1130614079426416773 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🧠", custom_id = "brainstormers~", style = discord.ButtonStyle.secondary)
  async def button5(self, interaction, button):
    role = 1130614206408962058 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🎵", custom_id = "Music~", style = discord.ButtonStyle.secondary)
  async def button6(self, interaction, button):
    role = 1130749504245747774 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)    
  


  @discord.ui.button(label = "❌", custom_id = "14-18", style = discord.ButtonStyle.secondary)
  async def button7(self, interaction, button):
    role = 1130746241198850131 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True) 


  @discord.ui.button(label = "✅", custom_id = "18+", style = discord.ButtonStyle.secondary)
  async def button8(self, interaction, button):
    role = 1130746378692341792 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "💀", custom_id = "25-30", style = discord.ButtonStyle.secondary)
  async def button9(self, interaction, button):
    role = 1130746480660062309 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)



  @discord.ui.button(label = "👀", custom_id = "30+", style = discord.ButtonStyle.secondary)
  async def button10(self, interaction, button):
    role = 1130749389497970800 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "😘", custom_id = "Bump", style = discord.ButtonStyle.secondary)
  async def button11(self, interaction, button):
    role = 1131362847625056256 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🫠", custom_id = "Weird_Talkers", style = discord.ButtonStyle.secondary)
  async def button12(self, interaction, button):
    role = 1131363802684866650 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)         


  @discord.ui.button(label = "🎉", custom_id = "Welcomers", style = discord.ButtonStyle.secondary)
  async def button13(self, interaction, button):
    role = 1131948684230283406 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "🙈", custom_id = "Selfie", style = discord.ButtonStyle.secondary)
  async def button14(self, interaction, button):
    role = 1131955006673780808 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)


  @discord.ui.button(label = "😎", custom_id = "Movie/Anime", style = discord.ButtonStyle.secondary)
  async def button15(self, interaction, button):
    role = 1132007404817633281 #put your role id here
    user = interaction.user
    if role in [y.id for y in user.roles]:
      await user.remove_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have removed a role!", ephemeral = True)
    else:
      await user.add_roles(user.guild.get_role(role))
      await interaction.response.send_message("You have added a role!", ephemeral = True)    
   