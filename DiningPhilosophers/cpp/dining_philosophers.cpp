#include <algorithm>
#include <array>
#include <chrono>
#include <format>
#include <iostream>
#include <mutex>
#include <random>
#include <string>
#include <string_view>
#include <thread>

const int timeScale = 42;  // scale factor for the philosophers task duration

void Message(std::string_view message)
{
    std::cout << message << std::endl;
}

struct ChopStick {
    std::mutex mutex;
};

struct Dinner {
    std::array<ChopStick, 5> sticks;
    ~Dinner() { Message("Dinner is over"); }
};

class DiningPhilosopher
{
    std::mt19937 rng{std::random_device {}()};

    const std::string name;
    ChopStick& left;
    ChopStick& right;
    std::jthread worker;

    void live();
    void dine();
    void ponder();
public:
    Philosopher(std::string name_, Fork& l, Fork& r)
    : name(std::move(name_)), left(l), right(r), worker(&Philosopher::live, this)
    {}
    ~Philosopher() = default;
};

void Philosopher::live()
{
    for(;;) // run forever
    {
        {
            std::scoped_lock dine_lock(left.mutex, right.mutex);
            dine();
        }
        
        ponder();
    }
}

void Philosopher::dine()
{
    Message(name + " started eating.");

    thread_local std::array<const char*, 3> foods {"chicken", "rice", "soda"};
    thread_local std::array<const char*, 3> reactions {
        "I like this {}!", "This {} is good.", "Mmm, {}..."
    };
    std::shuffle(foods.begin(), foods.end(), rng);
    std::shuffle(reactions.begin(), reactions.end(), rng);
    
    constexpr size_t buf_size = 64;
    char buffer[buf_size];
    for(int i = 0; i < 3; ++i) {
        std::this_thread::sleep_for(std::chrono::milliseconds(dist(rng) * timeScale));
        std::format_to_n(buffer, buf_size, reactions[i], foods[i]);
        Message(name + ": " + buffer);
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(dist(rng)) * timeScale);

    Message(name + " finished and left.");
}

void Philosopher::ponder()
{
    static constexpr std::array<const char*, 5> topics {{
        "politics", "art", "meaning of life", "source of morality", "how many straws makes a bale"
    }};
    thread_local std::uniform_int_distribution<> wait(1, 6);
    thread_local std::uniform_int_distribution<> dist(0, topics.size() - 1);
    while(dist(rng) > 0) {
        std::this_thread::sleep_for(std::chrono::milliseconds(wait(rng) * 3 * timeScale));
        Message(name + " is pondering about " + topics[dist(rng)] + ".");
    }
    std::this_thread::sleep_for(std::chrono::milliseconds(wait(rng) * 3 * timeScale));
    Message(name + " is hungry again!");
}

int main()
{
    Dinner dinner;
    Message("Dinner started!");

    std::array<Philosopher, 5> philosophers {{
            {"Aristotle",   dinner.forks[0], dinner.forks[1]},
            {"Democritus",  dinner.forks[1], dinner.forks[2]},
            {"Plato",       dinner.forks[2], dinner.forks[3]},
            {"Pythagoras",  dinner.forks[3], dinner.forks[4]},
            {"Socrates",    dinner.forks[4], dinner.forks[0]},
    }};
    Message("It is dark outside...");
}
