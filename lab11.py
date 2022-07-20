"""Estatísticas de notícias.

Esse módulo lê arquivos de notícias devidamente formatados e gera um relatório
para cada notícia, além de um relatório final."""


from typing import List, Union


def average(
        sum: int,
        quantity: int) -> int:
    """Calcula a média simples.

    Restringe-se a casos em que seu resultado é um número inteiro.
    """
    return int(sum / quantity)


def read_news_files() -> List[Union[int, str]]:
    """Lê os arquivos das notícias, de modo a obter seus metadados.

    Returns:
        Uma lista com inteiros e strings, que são os dados a serem utilizados
        na confecção do relatório final.
    """
    total_readers, total_ad_clicks, total_paragraphs = 0, 0, 0
    file_count = int(input())
    for counter in range(file_count):
        file = input()
        with open(file, "r") as news:
            data_lines = news.readlines()
        readers = int(data_lines[2].split(": ")[1])
        readers_end = int(data_lines[3].split(": ")[1])
        ad_clicks = int(data_lines[4].split(": ")[1])
        time = int(data_lines[5].split(": ")[1])
        paragraphs = len(data_lines[6:])
        total_readers += readers
        total_ad_clicks += ad_clicks
        total_paragraphs += paragraphs
        if counter == 0:
            max_readers = readers
            max_readers_end = readers_end
            title = data_lines[1].split(": ")[1].strip()
            max_readers_title = title
            max_readers_end_title = title
            max_time = time
        else:
            if readers > max_readers:
                max_readers = readers
                max_readers_title = data_lines[1].split(": ", 1)[1].strip()
            if readers_end > max_readers_end:
                max_readers_end = readers_end
                title = data_lines[1].split(": ", 1)[1].strip()
                max_readers_end_title = title
            if time > max_time:
                max_time = time
        generate_report(data_lines)
    return file_count, total_readers, max_readers_title, max_readers, \
        max_readers_end_title, max_readers_end, total_ad_clicks, max_time, \
        total_paragraphs


def generate_report(data_lines: List[str]) -> None:
    """Gera um relatório individual para uma notícia.

    Args:
        data_lines
            É a lista das linhas do arquivo da notícia."""
    id_number = data_lines[0][5:].strip()
    news_report = "relatorio_" + id_number + ".txt"
    id_line = data_lines[0]
    with open(news_report, "w") as report:
        report.write(id_line)
        report.write("".join(data_lines[2:6]).strip())


def generate_final_report(
        file_count: int,
        total_readers: int,
        max_readers_title: str,
        max_readers: int,
        max_readers_end_title: str,
        max_readers_end: int,
        total_ad_clicks: int,
        max_time: int,
        total_paragraphs: int) -> None:
    """Gera um relatório final, que possui as diversas estatísticas acerca
    de todas as notícias relatadas.

    Args:
        file_count:
            Número de arquivos de notícia que devem ser lidos.
        total_readers:
            Número total de leitores de todas as notícias.
        max_readers_title:
            Título da notícia com mais leitores.
        max_readers:
            Número de leitores da notícia com mais leitores.
        max_readers_end_title:
            Título da notícia com mais leitores que leram até o fim.
        max_readers_end:
            Número de leitores que leram até o fim a notícia com mais leitores
            que leram até o fim.
        total_ad_clicks:
            Número total de cliques em anúncios das notícia.
        max_time:
            Maior tempo de permanência em uma notícia.
        total_paragraphs:
            Número total de parágrafos de todas as notícias.
    """
    with open("relatorio_final.txt", "w") as final:
        final.write(
            str(average(total_readers, file_count)) + "\n"
        )
        final.write(
            "\"" + max_readers_title + "\" " + str(max_readers) + "\n"
        )
        final.write(
            "\"" + max_readers_end_title + "\" " + str(max_readers_end) + "\n"
        )
        final.write(
            str(average(total_ad_clicks, file_count)) + "\n"
        )
        final.write(
            str(max_time) + "\n"
        )
        final.write(
            str(average(total_paragraphs, file_count))
        )


def main() -> None:
    """Executa o programa principal."""
    generate_final_report(*read_news_files())


if __name__ == "__main__":
    main()
