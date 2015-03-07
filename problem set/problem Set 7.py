### PART I: DATA STRUCTURE DESIGN

class NewsStory(object):
    def __init__(self,guid,title,subject,summary,link):
        self.guid=guid
        self.title=title
        self.subject=subject
        self.summary=summary
        self.link=link
    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):  
        return self.summary
    def getLink(self):
        return self.link
		
		
		
### PART II: WORD TRIGGERS

class WordTrigger(Trigger):
 
    def __init__(self, word):
        self.word = word.lower()
 
    def isWordIn(self, text):
        new_text = ''
        sample = string.punctuation
        for i in sample:
            text = text.replace(i,' ')
        text = text.lower()
             
        text = text.split(' ')
       
        return self.word in text
 
           
# TODO: TitleTrigger
 
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
       
 
# TODO: SubjectTrigger
 
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
   
   
# TODO: SummaryTrigger
 
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

		

		
### PART II: COMPOSITE TRIGGERS

class WordTrigger(Trigger):
 
    def __init__(self, word):
        self.word = word.lower()
 
    def isWordIn(self, text):
        new_text = ''
        sample = string.punctuation
        for i in sample:
            text = text.replace(i,' ')
        text = text.lower()
             
        text = text.split(' ')
       
        return self.word in text
 
           
# TODO: TitleTrigger
 
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        # Enter your code for WordTrigger, TitleTrigger,
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.t = trigger
 
    def evaluate(self, story):
        return not self.t.evaluate(story)
   
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)
   
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2
 
    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)
		

		
### PART II: PHRASE TRIGGERS

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
       if self.phrase in story.getTitle():
          return True
       elif self.phrase in story.getSubject():
            return True
       elif self.phrase in story.getSummary():
            return True
       else:
            return False
   
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def removePunc(const):
        '''Where const is the string to convert  '''
        import string
        punc = string.punctuation
        for i in punc:
            const = const.replace(i, ' ')
        return const
    def isWordIn(self, text):
            text = text.lower()
            self.word = self.word.lower()
            for i in string.punctuation:
                text = text.replace(i,' ')
            words = text.split(' ')
           
            found = False
            if self.word in words:
                found = True
            return found
 
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
 
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
   
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
		
		
		
		
### PART III: FILTERING

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
       if self.phrase in story.getTitle():
          return True
       elif self.phrase in story.getSubject():
            return True
       elif self.phrase in story.getSummary():
            return True
       else:
            return False
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def removePunc(const):
        '''Where const is the string to convert  '''
        import string
        punc = string.punctuation
        for i in punc:
            const = const.replace(i, ' ')
        return const
    def isWordIn(self, text):
            text = text.lower()
            self.word = self.word.lower()
            for i in string.punctuation:
                text = text.replace(i,' ')
            words = text.split(' ')
           
            found = False
            if self.word in words:
                found = True
            return found
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())
   
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())
def filterStories(stories, triggerlist):
    """
   Takes in a list of NewsStory-s.
   Returns only those stories for whom
   a trigger in triggerlist fires.
   """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    # Feel free to change this line!
##  return stories
    res = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                res.append(story)
                break
    return res
	

	
### PART IV: USER-SPECIFIED TRIGGERS

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.
 
    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")
 
    Modifies triggerMap, adding a new key-value pair for this trigger.
 
    Returns: None
    """
    # TODO: Problem 11
    if triggerType == "TITLE":
        triggerMap[name] = TitleTrigger(params[0])
 
    elif triggerType == "SUBJECT":
        triggerMap[name] = SubjectTrigger(params[0])
 
    elif triggerType == "SUMMARY":
        triggerMap[name] = SummaryTrigger(params[0])
 
    elif triggerType == "NOT":
        triggerMap[name] = NotTrigger(triggerMap[params[0]])
 
    elif triggerType == "AND":
        triggerMap[name] = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "OR":
        triggerMap[name] = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
 
    elif triggerType == "PHRASE":
        triggerMap[name] = PhraseTrigger(' '.join(params))
 
    return triggerMap[name]
