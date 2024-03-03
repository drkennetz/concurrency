#ifndef PHILOSOPHER_HPP
#define PHILOSOPHER_HPP

#include <string>
#include <string_view>
#include <thread>
#include <array>

struct ChopStick {
    std::mutex mutex;
};

struct Dinner {
    std::array<ChopStick, 5> sticks;
    ~Dinner();
};

class DiningPhilosopher {
public:
    Philosopher(std::string name, Fork& l, Fork& r)
      : rng_(std::random_device{}())
      , name_(std::move(name))
      , leftStick_(l)
      , rightStick_(r)
      , worker_(&DiningPhilosopher::live, this)
    {
    }
    ~Philosopher();

private:
    std::mt19937 rng_;
    const std::string name_;
    ChopStick& leftStick_;
    ChopStick& rightStick_;
    std::jthread worker_;
};

#endif // PHILOSOPHER_HPP
