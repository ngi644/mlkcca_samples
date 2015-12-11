# encoding: utf-8
from argparse import ArgumentParser
import feedparser
from milkcocoa import milkcocoa as mlkcca

__author__ = 'ngi644'


def get_rss(url):
    """
    RSS取得

    :param str url: RSSのURL
    :return: RSSの辞書オブジェクト
    :rtype: dict
    """

    return feedparser.parse(url)


def add_record(url, link, title):
    """
    milkcocoaへデータの登録

    :param str url: RSSのURL
    :param str link: 記事のアドレス
    :param unicode title: 記事のタイトル
    """

    mlk_cnt = mlkcca.Milkcocoa.connectWithApiKey({app_id}, {key}, {secret}, useSSL=False)
    rss_ds = mlk_cnt.datastore(u'rss')
    rss_ds.push(dict(url=url, link=link, title=title))


if __name__ == '__main__':
    parser = ArgumentParser(description='Add RSS to the Milkcocoa Datastore')
    parser.add_argument('-i', '--rss_url',
                        type=str, required=True,
                        help=u'RSS URL')
    args = parser.parse_args()
    url = args.rss_url

    result = get_rss(url)

    for entry in result.entries:
        link = entry.link
        title = entry.title
        add_record(url, link, title)

    print('Done')