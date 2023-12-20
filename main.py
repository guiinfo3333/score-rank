from external.request import Request

if __name__ == '__main__':
    request = Request()
    # request.getStatistics("190160")

    matches_without_stats = request.get_match_id(10)
    for match_id in matches_without_stats:
        request.getStatistics(match_id)

    # request.obter_times(71, 2015,2022)
    # request.obter_partida(71, 2015, 2022)
