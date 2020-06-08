'''
a cog utilizing l of y selected responses 
'''

from random import choice
import asyncio

import discord as d 
from discord.ext import commands

from util import lists as l

class basicReplies(commands.Cog):
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.name = kwargs.get('username')

    @commands.command(pass_context=True, aliases=['goodbye'])
    async def bye(self, ctx, *, member: d.Member = None):
        '''a basic goodbye command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            gbye = choice(l.bye)
            await self.bot.say(gbye)
            return

        if member.id == '422901925034459147':
            await self.bot.say('I\'m not going anywhere though')
        elif member.id == ctx.message.author.id:
            await self.bot.say('where are you going?\n can\'t just say bye to yourself')
        elif member.id == '313168485591154688':
            await self.bot.say('later dad!')
        else:
            gbye_mention = choice(l.byeMention)
            await self.bot.say(gbye_mention.format(member.display_name))

    @commands.command()
    async def choose(self, *choices: str):
        '''a command used to choose between different options'''
        #split choices with , using roll as ref
        rand_line = choice(l.botRandLine)
        await self.bot.say(rand_line + ' __'+choice(choices)+'__')

    @commands.command(pass_context=True, aliases=['8ball'])
    async def eightball(self, ctx, question: str):
        '''an 8ball that gives a output'''
        await ctx.trigger_typing()
        await asyncio.sleep(1)
        await ctx.send(choice(l.eightBall))

    @commands.command(pass_context=True)
    async def _f(self, ctx, *, member: d.Member = None):
        '''a basic command that gives a f message'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        if member is None:
            respect = choice(l.respect)
            await self.bot.say(respect)
            return

        if member.id == '422901925034459147':
            await self.bot.say('gimme an f spam y\'all')
        else:
            respect = choice(l.respect)
            await self.bot.say(respect)
            return

    @commands.command(pass_context=True, aliases=['gm', 'morning'])
    async def goodmorning(self, ctx, *, member: d.Member = None):
        '''a basic goodmorning command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            gmorn = choice(l.morning)
            await self.bot.say(gmorn)
            return

        if member.id == '422901925034459147':
            await self.bot.say('good morning to you too')
        elif member.id == ctx.message.author.id:
            await self.bot.say('nobody to say goodmorning to you?\nthat\'s lowkey sad, dude')
        elif member.id == '313168485591154688':
            await self.bot.say('g\' morning dad')
        else:
            morning_mention = choice(l.morningMention)
            await self.bot.say(morning_mention.format(member.display_name))

    @commands.command(pass_context=True, aliases=['gn'])
    async def goodnight(self, ctx, *, member: d.Member = None):
        '''a basic goodnight command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            night = choice(l.night)
            await self.bot.say(night)
            return

        if member.id == '422901925034459147':
            await self.bot.say('good night, friend')
        elif member.id == ctx.message.author.id:
            await self.bot.say('saying goodnight to yourself is pretty weird dude')
        elif member.id == '313168485591154688':
            await self.bot.say('night dad')
        else:
            night_mention = choice(l.nightMention)
            await self.bot.say(night_mention.format(member.display_name))

    @commands.command(pass_context=True, aliases=['hbd'])
    async def happybirthday(self, ctx, *, member: d.Member = None):
        '''a basic command that gives a happy birthday message'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            await self.bot.say('so who\'s birthday is it then?')
            return

        if member.id == '422901925034459147':
            await self.bot.say('I\'ve never been born tho')
        elif member.id == '313168485591154688':
            await self.bot.say('Happy Birthday dad!')
        else:
            hb = choice(l.bDayMessage)
            await self.bot.say(hb.format(member.display_name))

    @commands.command(pass_context=True, aliases=['hi', 'hey'])
    async def hello(self, ctx, *, member: d.Member = None):
        '''a basic greeting command'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            greeting = choice(l.greetNoMention)
            await self.bot.say(greeting)
            return

        if member.id == '422901925034459147':
            await self.bot.say('hi.. me?')
        elif member.id == ctx.message.author.id:
            await self.bot.say('trying to say hi to yourself? Kinda weird, dude')
        elif member.id == '313168485591154688':
            await self.bot.say('HI DAD!')
        else:
            greet_mention = choice(l.greetMention)
            await self.bot.say(greet_mention.format(member.display_name))

    @commands.command(pass_context=True)
    async def insult(self, ctx, *, member: d.Member = None):
        '''a command that sends insults'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            await self.bot.say('tell me who to insult, dingus')
            return

        if member.id == '422901925034459147':
            await self.bot.say('can\'t insult perfection lol')
        elif member.id == '313168485591154688' and member.id == ctx.message.author.id:
            await self.bot.say('why are you asking me to insult you, dude? Lol')
        elif member.id == ctx.message.author.id:
            await self.bot.say('soooooo you\'re asking me to insult you? That\'s just you insulting yourself, dude.')
        elif member.id == '313168485591154688':
            insult = choice(l.insultDad)
            await self.bot.say(insult.format(member.display_name))
        else:
            insult = choice(l.insults)
            await self.bot.say(insult.format(member.display_name))

    @commands.command(pass_context=True)
    async def kill(self, ctx, *, member: d.Member = None):
        '''a command used to "kill" another member'''
        await ctx.trigger_typing()
        if member is None:
            message = choice(l.killNoMention)
            await ctx.send(message)
        
        elif member.id == 699160052015300649:
            message = choice(l.killSelf)
            await ctx.send(message)
        elif member.id == 184715297536606208 and member.id == ctx.message.author.id:
            await ctx.send('**NO**')
        elif member.id == 313168485591154688 and member.id == ctx.message.author.id:
            await ctx.send('I\'m not killing you dad lol')
        elif member.id == ctx.message.author.id:
            await ctx.send('who do I look like, Jack Kevorkian?\nno assisted suicide lol')
        elif member.id == 184715297536606208:
            await ctx.send('I\'m not going to hurt my mom, assface')
        elif member.id == 313168485591154688:
            message = choice(l.killDad)
            await ctx.send(message)
        
        else:
            kill_message = choice(l.killReply)
            await ctx.send(kill_message.format(member.display_name))

    @commands.command(pass_context=True)
    async def lol(self, ctx, *, member: d.Member = None):
        '''a command Sany rode my ass about'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            lol = choice(l.LOL)
            await self.bot.say(lol)
            return

        if member.id == '422901925034459147':
            await self.bot.say('why do you lol at me?')
        else:
            await self.bot.say('{0} {1}'.format(member.mention, choice(l.LOL)))

    @commands.command(pass_context=True, aliases=['luv'])
    async def love(self, ctx, *, member: d.Member = None):
        '''a basic command that sends a love message'''
        await self.bot.send_typing(ctx.message.channel)
        if member is None:
            love_message = choice(l.loveNoMention)
            await self.bot.say(love_message)
            return

        if member.id == '422901925034459147':
            await self.bot.say('I love me too')
        elif member.id == ctx.message.author.id:
            love_self = choice(l.selfLove)
            await self.bot.say(love_self.format(member.display_name))
        else:
            love_mention = choice(l.loveMsg)
            await self.bot.say(love_mention.format(member.display_name))

    @commands.command(pass_context=True, aliases=['MOTIVATE', 'Motivate'])
    async def motivate(self, ctx):
        '''a basic command that sends a motivational message'''
        await self.bot.send_typing(ctx.message.channel)
        motivate_message = choice(l.motivateLog)
        embed = d.Embed(
            color=0x000000)
        embed.add_field(name='Quote', value=motivate_message)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True, aliases=['name'])
    async def _name(self, ctx, *, member: d.Member = None):
        '''a basic command that gives a set of words for  names'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        name_1 = choice(l.nOne)
        name_2 = choice(l.nTwo)
        name_3 = choice(l.nThree)

        name = name_1 + ' ' + name_2 + ' ' + name_3

        if member is None:
            member = ctx.message.author
            no_mention = choice(l.sayNoMention).format(member.display_name)
            await self.bot.say(no_mention + ' __{}__'.format(name))
            return
        if member.id == '422901925034459147':
            await self.bot.say('my name is ri0t-bot lol')
        else:
            mention = choice(l.sayMention).format(member.display_name)
            await self.bot.say(mention + ' ' + name)

    @commands.command(pass_context=True)
    async def oof(self, ctx):
        '''a basic oof command'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        om = choice(l.oof)
        await self.bot.say(om)

    @commands.command(pass_context=True)
    async def rip(self, ctx):
        '''a basic rip command'''
        await ctx.trigger_typing()
        _choice = choice(l.rip)
        await ctx.send(_choice)

    @commands.command(pass_context=True, aliases=['st'])
    async def showerthoughts(self, ctx):
        '''sends a shower thought'''
        await self.bot.send_typing(ctx.message.channel)
        await asyncio.sleep(0.3)
        st = choice(l.dumbStuff)
        await self.bot.say(st)

def setup(bot):
    '''cog setup'''
    bot.add_cog(basicReplies(bot))
    print('basic list commands ready')
    