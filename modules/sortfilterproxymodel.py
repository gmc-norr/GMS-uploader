from PySide6.QtCore import Qt, QSortFilterProxyModel


class MultiFilterMode:
    AND = 0
    OR = 1


class MultiSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.filters = {}
        self.multi_filter_mode = MultiFilterMode.OR

    def setFilterByColumn(self, column, regex):
        if isinstance(regex, str):
            # regex = re.compile(regex)
            self.filters[column] = regex
            self.invalidateFilter()

    def setFilterByColumns(self, columns, regex):
        for column in columns:
            self.filters[column] = regex
            self.invalidateFilter()

    def clearFilter(self, column):
        del self.filters[column]
        self.invalidateFilter()

    def clearFilters(self):
        self.filters = {}
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        if not self.filters:
            return True

        results = []
        for key, regex in self.filters.items():
            text = ''
            index = self.sourceModel().index(source_row, key, source_parent)
            if index.isValid():
                text = self.sourceModel().data(index, Qt.DisplayRole)
                if text is None:
                    text = ''

            if regex.match(text).hasMatch():
                results.append(True)
            else:
                results.append(False)

        if self.multi_filter_mode == MultiFilterMode.OR:
            return any(results)

        return all(results)


class CheckedFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.filters = {}

    def setFilterByColumn(self, column, filter_int):
        self.filters[column] = filter_int
        print(self.filters)
        self.invalidateFilter()

    def clearFilters(self):
        self.filters = {}
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        print("accept")
        if not self.filters:
            return True

        results = []
        for key, filter_value in self.filters.items():
            data_value = 0
            index = self.sourceModel().index(source_row, key, source_parent)
            if index.isValid():
                item = self.sourceModel().data(index, Qt.DisplayRole)
                if data_value is None:
                    data_value = 0

            if filter_value == data_value:
                results.append(True)
            else:
                results.append(False)

        return all(results)
