# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider

print('===========BEM VINDO AO MLSCRAPPER1.0')
busca = str(input('============DIGITE SUA BUSCA:'))
class MLSpider(Spider):
    name = 'mlivre'
    lol = str('https://lista.mercadolivre.com.br/'+busca)
    start_urls = [lol]

    def parse(self, response):
        resposta = response.xpath('//ol/li')
        items = []
        for elemento in resposta:
            file = open("savefile.txt","a")
            Imagem = ' '.join(elemento.xpath('.//div[contains(@class, "image-content")]/a/@href').extract())
            Nome = ' '.join(elemento.xpath(".//div/h2/a/span/text() " ).extract())
            Price = ' '.join(elemento.xpath(".//div/div/span[@class='price__fraction']/text()" ).extract())
            Desconto = ' '.join(elemento.xpath(".//div[contains(@class, 'item__discount')]/text()").extract())
            Vendedor = ' '.join(elemento.xpath(".//div[contains(@class,'item__brand')]//span/text()").extract())
            ItensVendidos = ' '.join(elemento.xpath(".//div[contains(@class,'item__condition')]/text()").extract())
            InfoAdicional = ' '.join(elemento.xpath(".//p[contains(@class, 'stack-item-info')]/text()").extract())
            items.append(Imagem)
            items.append(Nome)
            items.append(Price)
            items.append(Desconto)
            items.append(Vendedor)
            items.append(ItensVendidos)
            items.append(InfoAdicional)
            file.write(str(Imagem))
            file.write(str(Nome))
            file.write(str(Price))
            file.write(str(Desconto))
            file.write(str(Vendedor))
            file.write(str(ItensVendidos))
            file.write(str(InfoAdicional))
            file.close()
            
        pass
        file = open("savefile.txt","w")
        file.write(str(items))
        file.close()
        while len(items) > 1:
            print('Imagem: ', items[0])
            print('Nome: ', items[1])
            print('Price: ', items[2])
            print('Desconto: ', items[3])
            print('Vendedor: ', items[4])
            print('ItensVendidos: ', items[5])
            print('InfoAdicional: ', items[6])
            print('\n')
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            items.pop(0)
            pass

