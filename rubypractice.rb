=begin
name = "mike"
age = 30
is_tall = true

puts "Your name is " + name

puts 3.14.to_i #to int

puts 3.to_f #to float

puts 3.0.to_s #to string

greeting = "Hello"
#indexes:   01234
puts greeting.length
puts greeting[0]
puts greeting.include? "llo" #is this included in given var/string?
puts greeting[1,3] #start at e, end at l (e l l)


# user input

puts "Enter your name: "
name = gets.chomp #keyword gets is for user input
#keyword chomp removes newline char
puts "Hello #{name}, how are you"

puts "first num: "
fNum = gets
puts "second num: "
sNum = gets
totNum = fNum.to_f + sNum.to_f
puts "total: #{totNum}"




# arrays

lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0]
#indexes         0  1   2         3   4   5

puts lucky_numbers[2,3] #2 is starting index, 3 is length
puts lucky_numbers[2..4] #collects indexes 2 through 4, same
						 #output as above

friends = []
friends.push("Oscar")
friends.push("Angela") #adds element to array
friends.push("Kevin")

puts friends

puts friends.reverse #reverse order

puts friends.sort #alphabetical order

puts friends.include? "Oscar"

friends.pop #removes last element



# methods

def add_numbers(num1, num2=99) #can set default value
	return num1 + num2
end 

sum = add_numbers(4, 3)
puts sum



# switch

my_grade = "A"

case my_grade
	when "A"
		puts "Pass"
	when "F"
		puts "Fail"
	else
		puts "Invalid"
end



# dictionaries

test_grades = {
	"Andy" => "B+",
	:Stanley => "C",
	3 => 95.2
}

test_grades["Andy"] = "B-"
puts test_grades["Andy"]
puts test_grades[:Stanley]
puts test_grades[3] #int represents key, not index


# while loops

index = 1
while index <= 5
	puts index
	index += 1
end


# for loops

for index in 0..5
	puts index
end

5.times do |index|
	puts index
end


# exception handling

 #num = 10/0 <- error bc of zero division

begin 
	num = 10/0
rescue
	puts "Error"
end

begin 
	#puts bad_variable
	num = 10/0
rescue ZeroDivisionError
	puts "Error"
rescue
	puts "All other errors"
end

raise "Made up Exception" <- create own exception



#objects in Ruby

class Book
	attr_accessor :title, :author #define attributes

	def readBook()
		puts "Reading #{self.title} by #{self.author}"
	end
end

book1 = Book.new()
book1.title = "Harry Potter"
book1.author = "JK Rowling"

book1.readBook()

puts book1.title	



#constructors

class Book
	attr_accessor :title, :author
	def initialize(title, author)
		@title = title
		@author = author
	end

	def readBook()
		puts "Reading #{self.title} by #{@author}"
	end
end

book1 = Book.new("Harry Potter", "JK Rowling")

=end

#getter + setter

class Book
	attr_accessor :title, :author
	def initialize(title, author)
		self.title = title
		@author = author
	end

	def title=(title)
		puts "Set"
		@title=title
	end

	def title
		puts "Get"
	@title=title

end



