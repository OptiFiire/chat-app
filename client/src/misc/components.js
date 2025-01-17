import * as lucideIcons from 'lucide-vue-next';

export default {
    install(app) {
        const uiComponents = import.meta.glob('@/components/**/**/*.vue', { eager: true });
        const iconComponents = [
            'Search',
            'Plus',
            'CircleUser',
            'LogOut',
            'SendHorizontal'
        ];

        Object.entries(uiComponents).forEach(([path, component]) => {
            try {
                const componentName = path.split('/').pop()?.replace('.vue', '');
                app.component(componentName, component?.default);
            } catch (e) {
                console.error(e);
            }
        });

        iconComponents.forEach((iconName) => {
            const iconComponent = lucideIcons[iconName];
            if (iconComponent) {
                app.component(iconName, iconComponent);
            } else {
                console.warn(`Icon "${iconName}" does not exist in lucide-vue-next.`);
            }
        });
    }
};
