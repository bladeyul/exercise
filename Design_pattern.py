#单例模式
class Singleton(object):

	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance=super(Singleton,cls).__new__(cls)
		return cls.instance

#单例模式懒加载
class Singleton2(object):

	__instance=None
	def __init__(self):
		if not Singleton2.__instance:
			pass
		else:
			return self.getInstance()

	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance=Singleton()
		return cls.__instance

#Monostate模式
class Borg(object):

	__shared_dict={}

	def __init__(self):
		self.__dict__=self.__shared_dict

class Borg2(object):
	__shared_dict={}
	def __new__(cls,*args,**kwargs):
		obj=super(Borg,cls).__new__(cls,*args,**kwargs)
		obj.__dict__=cls.__shared_dict
		return obj

#基于元类的实现
class MetaSingleton(type):
	_instances={}
	def __call__(cls,*args,**kwargs):
		if cls not in cls._instances:
			cls._instances[cls]=super(MetaSingleton,cls).__call__(*args,**kwargs)
		return cls._instances[cls]

#简单工厂模式
from abc import ABCMeta,abstractmethod
class Animal(metaclass=ABCMeta):
	@abstractmethod
	def do_say(self):
		pass

class Dog(Animal):
	def do_say(self):
		print("wang wang")

class Cat(Animal):
	def do_say(self):
		print("Meow Meow")

class ForestFactory(object):
	def make_sound(self,object_type):
		return eval(object_type().do_say())

#工厂方法
class Section(metaclass=ABCMeta):
	@abstractmethod
	def describe(self):
		pass

class PersonalSection(Section):
	def describe(self):
		print("PersonalSection")

class AlbumSection(Section):
	def describe(self):
		print("AlbumSection")

class PatentSection(Section):
	def describe(self):
		print("PatentSection")

class PublicationSection(Section):
	def describe(self):
		print("PublicationSection")

class Profile(metaclass=ABCMeta):
	def __init__(self):
		self.sections=[]
		self.createProfile()

	@abstractmethod
	def createProfile(self):
		pass

	def getSections(self):
		return self.sections

	def addSections(self,section):
		self.sections.append(section)

class Linkedin(Profile):
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(PatentSection())
		self.addSections(PublicationSection())

class Facebook(Profile):
	def createProfile(self):
		self.addSections(PersonalSection())
		self.addSections(AlbumSection())

#抽象工厂模式
class PizzaFactory(metaclass=ABCMeta):

	@abstractmethod
	def createVegPizza(self):
		pass

	@abstractmethod
	def createNonVegPizz(self):
		pass

class IndiaPizzaFactory(PizzaFactory):

	def createVegPizza(self):
		return DeluxVeggiePizza()

	def createNoneVegPizza(self):
		return ChickenPizza()

class USPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return MexicanVegPizza()

	def crateNonVegPizza(self):
		return HanPizza()


class VegPizza(metaclass=ABCMeta):
	@abstractmethod
	def prepare(self,VegPizza):
		pass

class NonVegPizza(metaclass=ABCMeta):
	@abstractmethod
	def serve(self,VegPizza):
		pass

class DeluxVeggiePizza(VegPizza):
	def prepare(self):
		print(type(self).__name__)

class ChickenPizza(NonVegPizza):
	def serve(self,VegPizza):
		print(type(self).__name__,type(VegPizza).__name__)

class MexicanVegPizza(VegPizza):
	def prepare(self):
		print(type(self).__name__)

class HanPizza(NonVegPizza):
	def serve(self,VegPizza):
		print(type(self).__name__,type(VegPizza).__name__)

class PizzaStore:

	def __init__(self):
		pass

	def makePizzas(self):
		for factory in [IndiaPizzaFactory(),USPizzaFactory()]:
			self.factory=factory
			self.NoneVegPizza=self.factory.createNonVegPizz()
			self.VegPizza=section.factory.createVegPizza()
			self.VegPizza.prepare()
			self.NoneVegPizza.serve(self.VegPizza)

#门面模式
class EventManager(object):
	def __init__(self):
		pass

	def arrange(self):
		self.hotelier=Hotelier()
		self.hotelier.bookHotel()

		self.florist=Florist()
		self.florist.setFlowerRequirements()

		self.caterer=Caterer()
		self.caterer.setCuisine()

		self.musician=Musician()
		self.musician.setMusicType()

class Hotelier(object):
	def __init__(self):
		pass

	def __isAvailable(self):
		return True

	def bookHotel(self):
		if self.__isAvailable():
			pass

class Floriest(object):

	def setFlowRequirements(self):
		pass

class Caterer:
	def setCuisine(self):
		pass

class Musician(object):
	def setMusicType(self):
		pass


class You(object):

	def askEventManager(self):
		em=EventManager()
		em.arrange()


#代理模式
class Actor(object):
	def __init__(self):
		self.isBusy=False

	def occupied(self):
		self.isBusy=True

	def avaliable(self):
		self.isBusy=False

	def getStatus(self):
		return self.isBusy

class Agent(object):

	def __init__(self):
		self.principal=None

	def work(self):
		self.actor=Actor()
		if self.actor.getStatus:
			self.actor.occupied()
		else:
			self.actor.avaliable()

#代理模式
class You:

	def __init__(self):
		self.debitCard=DebitCard()
		self.isPurchased=None

	def make_payment(self):
		self.isPurchased=self.debitCard.do_pay()

class Payment(metaclass=ABCMeta):

	@abstractmethod
	def do_pay(self):
		pass

class Bank(Payment):

	def __init__(self):
		self.card=None
		self.account=None

	def __getAccount(self):
		self.account=self.card
		return self.account

	def __hasFunds(self):
		return True

	def setCard(self,card):
		self.card=card

	def do_pay(self):
		if self.__hasFunds()
			return True
		else:
			return False

class DebitCard(Payment):
	def __init__(self):
		self.bank=Bank()

	def do_pay(self):
		self.bank.setCard(card)
		return self.bank.do_pay()

#观察者模式
class Subject:

	def __init__(self):
		self.__observers=[]

	def register(self,observer):
		self.__observers.append(observer)

	def notifyAll(self,*args,**kwargs):
		for observer in self.__observers:
			observer.notify(self,*args,**kwargs)

class Observer1:

	def __init__(self,subject):
		subject.register(self)

	def notify(self,subject,*args):
		print(type(self).__name__)

class Observer2:

	def __init__(self,subject):
		subject.register(self)

	def notify(self,subject,*args):
		print(type(self).__name__)

class NewPublisher:

	def __init__(self):
		self.__subscribes=[]
		self.__latestNews=None

	def attatch(self,subscriber):
		self.__subscribes.append(subscriber)

	def detach(self):
		return self.__subscribes.pop()

	def subscribes(self):
		return [type(x).__name__ for x in self.__subscribers]

	def notifySubscribers(self):
		for sub in self.__subscribes:
			sub.update()

	def addNews(self,news):
		self.__latestNews=news

	def getNews(self):
		return self.__latestNews

class Subscriber(metaclass=ABCMeta):

	@abstractmethod
	def update(self):
		pass

class SMSSubscriber:

	def __init__(self,publisher):
		self.publisher=publisher
		self.publisher.attatch(self)

	def update(self):
		print(self.publisher.getNews())

class EmailSubscriber:
	def __init__(self,publisher):
		self.publisher=publisher
		self.publisher.attatch(self)

	def update(self):
		print(self.publisher.getNews())

class AnyOtherSubscriber:

	def __init__(self,publisher):
		self.publisher=publisher
		self.publisher.attache(self)

	def update(self):
		print(self.publisher.getNews())

#命令模式
class Wizard():

	def __init__(self,src,rootdir):
		self.choices=[]
		self.rootdir=rootdir
		self.src=src

	def preferences(self,command):
		self.choices.append(command)

	def execute(self):
		for choice in self.choices:
			if list(choice.valus())[0]:
				print()

class Command(metaclass=ABCMeta):

	def __init__(self,recv):
		self.recv=recv

	def execute(self):
		pass

class ConcreteCommand(Command):
	def __init__(self,recv):
		self.recv=recv

	def execute(self):
		self.recv.action()

class Receiver:

	def action(self):
		print("receive")

class Invoker:
	def command(self,cmd):
		self.cmd=cmd

	def execute(self):
		self.cmd.execute()


class Order(metaclass=ABCMeta):

	@abstractmethod
	def execute(self):
		pass

class BusyStockOrder(Order):
	def __init__(self,stock):
		self.stock=stock

	def execute(self):
		self.stock.buy()

class SellStockOrder(Order):
	def __init__(self,stock):
		self.stock=stock

	def execute(self):
		self.stock.sell()

class StockTrade:
	def buy(self):
		print("buy")

	def sell(self):
		print("sell")

class Agent:
	def __init__(self):
		self.__orderQueue=[]
	def placeOrder(self,order):
		self.__orderQueue.append(order)
		order.execute()
#模板方法
class Compiler(metaclass=ABCMeta):
	@abstractmethod
	def collectSource(self):
		pass

	@abstractmethod
	def compileToObject(self):
		pass

	@abstractmethod
	def run(self):
		pass

	def compileAndRun(self):
		self.collectSource()
		self.compileToObject()
		self.run()

class IOSCompiler(Compiler):
	def collectSource(self):
		print("collect source")

	def compileToObject(self):
		prit("compiling code")

	def run(self):
		print("run")

class Trip(metaclass=ABCMeta):

	@abstractmethod
	def setTransport(self):
		pass

	@abstractmethod
	def day1(self):
		pass

	@abstractmethod
	def day2(self):
		pass

	@abstractmethod
	def day3(self):
		pass

	@abstractmethod
	def returnHome(self):
		pass

	def itinerary(self):
		self.setTransport()
		self.day1()
		self.day2()
		self.day3()
		self.returnHome()

class VeniceTrip(Trip):

	def setTransport(self):
		print("transport")

	def day1(self):
		print("day1")

	def day2(self):
		print("day2")

	def day3(self):
		print("day3")

	def returnHome(self):
		print("get home")

class MaldivesTrip(Trip):

	def setTransport(self):
		print("transport")

	def day1(self):
		print("day1")

	def day2(self):
		print("day2")

	def day3(self):
		print("day3")

	def returnHome(self):
		print("get home")

class TravelAgency:

	def arrange_trip(self,choice):

		if choice=="historical":
			self.trip=VeniceTrip()
			self.trip.itinerary()

#MVC模式
class Model(object):
	services={
		'email':{'number':1000,'prices':2,},
		'sms':{'number':1000,'proce':10,},
		'voice':{'number':1000,'proce':15,},
	}

class View(object):
	def list_services(self,services):
		for svc in services:
			print(svc)

	def list_pricing(self,services):
		for svc in services:
			print(Model.services[svc]['number'],
				Model.services[svc]['price'])

class Controller(object):
	def __init__(self):
		self.model=Model()
		self.view=View()

	def get_services(self):
		services=self.model.services.keys()
		return (self.view.list_services(services))

	def get_pricing(self):
		services=self.model.services.keys()
		return (self.view.list_pricing(services))

class Client:

	controller=Controller()
	controller.get_services()
	controller.get_pricing()


#状态模式
class State(metaclass=ABCMeta):

	@abstractmethod
	def Handle(self):
		pass

class ConcreteStateB(State):
	def Handle(self):
		print("ConcreteStateB")

class ConcreteStateA(State):
	def Handle(self):
		print("ConcreteStateA")

class Context(State):

	def __init__(self):
		self.state=None

	def getState(self):
		return self.state

	def setState(self,state):
		self.state=state

	def Handle(self):
		self.state.Handle()


class State(metaclass=ABCMeta):

	@abstractmethod
	def doThis(self):
		pass

class StartState(State):
	def doThis(self):
		print("TV switch on")

class StopState(State):
	def doThis(self):
		print("Tv switch off")

class TVContext(State):

	def __init__(self):
		self.state=None

	def getState(self):
		return self.state

	def setState(self,state):
		self.state=state

	def doThis(self):
		self.state.doThis()

class ComputerState(object):
	name="state"
	allowd=[]

	def switch(self,state):
		if state.name in self.allowd:
			self.__class__=state
		else:
			print("cannot switch "+state.name)

	def __str__(self):
		return self.name

class Off(ComputerState):
	name="off"
	allowed=['on']

class On(ComputerState):
	name='on'
	allowed=['off','suspend','hibernate']

class Suspend(ComputerState):
	name="suspend"
	allowd=['on']

class Hibernate(ComputerState):
	name="hibernate"
	allowd=['on']

class Computer(object):
	def __init__(self,model='HP'):
		self.model=model
		self.state=Off()

	def change(self,state):
		self.state.switch(state)





