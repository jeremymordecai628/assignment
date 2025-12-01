public class UniversityInheritanceDemo {

    public static void main(String[] args) {

        UndergraduateStudent student1 = new UndergraduateStudent("Byron Busisa", 21, "Software Engineering");
        UndergraduateStudent student2 = new UndergraduateStudent("Mandy", 19, "Business Management");
        PostgraduateStudent student3 = new PostgraduateStudent("Mordecai", 26, "Artificial Intelligence");
        Lecturer lecturer = new Lecturer("Dr Benard Ondara", 45, "Computer Science");

        // Parent class method
        student1.attendLecture();
        student2.attendLecture();
        student3.attendLecture();
        lecturer.attendLecture();

        // Undergraduate-specific behavior
        student1.registerForClubs();
        student2.registerForClubs();

        // Postgraduate-specific behavior
        student3.defendThesis();

        // Lecturer-specific behavior
        lecturer.teachCourse();
    }
}

// Parent Class (Superclass)
class UniversityMember {
    String name;
    int age;

    public UniversityMember(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void attendLecture() {
        System.out.println(name + " is attending a lecture.");
    }
}

// Subclass 1: Undergraduate Student
class UndergraduateStudent extends UniversityMember {
    String major;

    public UndergraduateStudent(String name, int age, String major) {
        super(name, age);
        this.major = major;
    }

    public void registerForClubs() {
        System.out.println(name + " is registering for clubs as an undergraduate.");
    }
}

// Subclass 2: Postgraduate Student
class PostgraduateStudent extends UniversityMember {
    String researchTopic;

    public PostgraduateStudent(String name, int age, String researchTopic) {
        super(name, age);
        this.researchTopic = researchTopic;
    }

    public void defendThesis() {
        System.out.println(name + " is preparing to defend a thesis on: " + researchTopic);
    }
}

// Subclass 3: Lecturer
class Lecturer extends UniversityMember {
    String department;

    public Lecturer(String name, int age, String department) {
        super(name, age);
        this.department = department;
    }

    public void teachCourse() {
        System.out.println(name + " is teaching a course in the " + department + " department.");
    }
}
