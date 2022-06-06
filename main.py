from textual.app import App
from textual.widgets import Placeholder, Button, Header, Footer, ScrollView


class MainApp(App):
    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        button1 = Button(label="Hello", name="button1")

        header = Header(tall=False)
        await self.view.dock(header)

        footer = Footer()
        await self.view.dock(footer, edge="bottom")

        await self.view.dock(Placeholder(name="footer"), edge="bottom", size=3)
        await self.view.dock(Placeholder(name="stats"), edge="left", size=40)
        await self.view.dock(Placeholder(name="message"), edge="right", size=40)
        await self.view.dock(Placeholder(name="grid"), edge="top")

        scroll_view = ScrollView(contents=Button(label="button2"))
        await self.view.dock(scroll_view)


MainApp.run(title="Fourier")
