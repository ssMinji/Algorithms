def solution(cacheSize, cities):
    runTime = 0
    if cacheSize == 0:
        runTime = len(cities) * 5
        return runTime

    cache_list = ['']*cacheSize

    for city in cities:
        city = city.lower()
        if city in cache_list:
            runTime += 1
            cache_list.remove(city)
            cache_list.append(city)
        else:
            cache_list.append(city)
            cache_list.pop(0)
            runTime += 5

    return runTime

print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))